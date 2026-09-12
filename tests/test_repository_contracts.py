"""Mutations exercise the actual preservation and package boundaries."""
from pathlib import Path
import shutil
import tempfile
import unittest

import check_repository as check


class PublicContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = check.ROOT
        cls.text = check.read(cls.root/'README.md')
        cls.cfg = check.contract(cls.root)

    def rejected(self, text, reason):
        errors = check.validate_readme(self.root, text)
        self.assertTrue(any(reason in e for e in errors), errors)

    def test_current_repository(self):
        result = check.check(self.root)
        self.assertEqual(result['result'], 'PASS', result)

    def test_complete_quick_start(self):
        self.rejected(self.text.replace('reserve effort for review.', '', 1), 'complete inline')

    def test_public_process_leakage(self):
        for leak in ('Stage 18','Stage N','feat/bootstrap','bootstrap progress','bootstrap sequence',
                     'production scaffold','maturity promotion','completion SHA','verification count',
                     'not-run','implemented later','not yet scaffolded','a'*40,
                     '[evidence](docs/research-logs/bootstrap-progress.md)'):
            with self.subTest(leak=leak):
                self.rejected(self.text+'\n'+leak+'\n', 'public-process leakage')

    def test_heading_order(self):
        text=self.text.replace('## Research capabilities','## Temporary heading',1)
        text=text.replace('## Research effort and evidence control','## Research capabilities',1)
        text=text.replace('## Temporary heading','## Research effort and evidence control',1)
        self.rejected(text,'sections/order')

    def test_missing_example(self):
        line=next(s for s in self.text.splitlines() if s.startswith('- **L2-03 —'))
        self.rejected(self.text.replace(line,'',1),'three-example progression')

    def test_duplicate_example(self):
        line=next(s for s in self.text.splitlines() if s.startswith('- **L3-02 —'))
        self.rejected(self.text.replace(line,line+'\n'+line,1),'three-example progression')

    def test_wrong_example_destination(self):
        a,b=self.cfg['examples'][:2]
        self.rejected(self.text.replace(a['path'],b['path'],1),'identity/link mismatch')

    def test_broken_local_link(self):
        self.rejected(self.text+'\n[Missing](missing-file.md)\n','broken local link')

    def test_broken_anchor(self):
        self.rejected(self.text+'\n[Missing](README.md#missing-anchor)\n','broken anchor')

    def test_substantive_skill_section(self):
        start=self.text.index('### `research-evaluate`')
        end=self.text.index('### `research-extension-pack-creator`',start)
        self.rejected(self.text[:start]+'### `research-evaluate`\n\nAudits.\n\n'+self.text[end:],
                      'substantive skill section')

    def test_positioning_preserved(self):
        self.rejected(self.text.replace('Conduct evidence-backed research','Collect some links',1),
                      'non-mechanical change')


class FileMutationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='deep-research-contract-')
        self.root = Path(self.tmp.name)/'repo'
        shutil.copytree(check.ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))
        self.cfg=check.contract(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_missing_public_surface(self):
        (self.root/self.cfg['examples'][0]['path']).unlink()
        self.assertTrue(any('surface count/path' in e for e in check.validate_examples(self.root)))
        self.assertTrue(any('broken local link' in e for e in check.validate_readme(self.root)))

    def test_sixteenth_primary_example(self):
        extra=self.root/'examples/level-1-extra/README.md'
        extra.parent.mkdir()
        extra.write_text('# Extra example\n')
        self.assertTrue(any('surface count/path' in e for e in check.validate_examples(self.root)))

    def test_each_exact_prompt(self):
        for example in self.cfg['examples']:
            with self.subTest(example=example['id']):
                path=self.root/example['path']
                original=check.read(path)
                path.write_text(original.replace('```text\n','```text\nChanged input. ',1))
                errors=check.validate_examples(self.root)
                self.assertIn('exact accepted prompt changed: '+example['id'],errors)
                path.write_text(original)

    def test_evaluation_and_output_contract(self):
        e=self.cfg['examples'][5]
        path=self.root/e['path']
        original=check.read(path)
        path.write_text(original.replace(e['negative_contract'],'',1).replace('- `'+e['expected_artefacts'][0]+'`','',1))
        errors=check.validate_examples(self.root)
        self.assertTrue(any('negative_contract' in x for x in errors),errors)
        self.assertTrue(any('missing required output' in x for x in errors),errors)

    def test_missing_command(self):
        (self.root/'skills/deep-research/commands/frame.md').unlink()
        errors=check.validate_packages(self.root)
        self.assertTrue(any('command ownership/count' in x for x in errors),errors)
        self.assertTrue(any('broken local link' in x for x in errors),errors)

    def test_command_write_boundary_removed(self):
        path=self.root/'skills/research-evaluate/commands/audit.md'
        path.write_text(check.read(path).replace('**Outputs and write scope.**','**Removed.**',1))
        self.assertTrue(any('Outputs and write scope' in e for e in check.validate_packages(self.root)))

    def test_reference_cannot_escape_skill(self):
        path=self.root/'skills/deep-research/SKILL.md'
        path.write_text(check.read(path)+'\n[External dependency](../../README.md)\n')
        self.assertTrue(any('link escapes boundary' in e for e in check.validate_packages(self.root)))

    def test_symlink_cannot_escape_skill(self):
        path=self.root/'skills/deep-research/references/external.md'
        path.symlink_to(self.root/'README.md')
        self.assertTrue(any('symlink escapes' in e for e in check.validate_packages(self.root)))

    def test_evidence_contract_drift(self):
        path=self.root/'skills/research-evaluate/references/evidence-contract.md'
        path.write_text(check.read(path)+'\nDrift.\n')
        self.assertIn('producer/evaluator evidence invariant drift',check.validate_packages(self.root))

    def test_historical_evidence_preserved(self):
        path=self.root/'docs/research-logs/2026-09-10-stage-12-progressive-examples.md'
        path.write_text(check.read(path)+'\nChanged historical decision.\n')
        self.assertTrue(any('accepted evidence changed' in e for e in check.validate_history(self.root)))

    def test_mit_required(self):
        (self.root/'LICENSE').write_text('A different licence.\n')
        self.assertIn('selected MIT licence text missing',check.validate_surfaces(self.root))


if __name__=='__main__':
    unittest.main()
