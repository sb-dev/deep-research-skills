"""Repair the labelled demonstration copy after independent diagnosis.

Original inputs, provisional package and production calculation/results are untouched.
Only the deliberately wrong denominator and its dependent fraction are corrected.
"""
import csv, hashlib, json
from pathlib import Path

BASE=Path(__file__).parent

def main():
    source=BASE/'demonstration-error.csv'
    with source.open(newline='') as f:
        reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
    target=('202507','powered','ALL','Fixed')
    key=lambda r:tuple(r[k] for k in ('snapshot','coverage','data_provider','repair_status'))
    selected=[r for r in rows if key(r)==target]
    assert len(selected)==1
    row=selected[0];before=dict(row)
    denominator=sum(int(r['count']) for r in rows if key(r)[:3]==target[:3])
    row['denominator_all_statuses']=str(denominator)
    row['share']=format(int(row['count'])/denominator,'.12f')
    out=BASE/'demonstration-repaired.csv'
    with out.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
    original=BASE/'provisional/results.csv'
    assert out.read_bytes()==original.read_bytes(), 'Repair must recover original without collateral changes'
    result={'target':target,'before':before,'after':dict(row),'changed_fields':['denominator_all_statuses','share'],'changed_rows':1,'unaffected_rows':len(rows)-1,'before_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'after_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'equals_unmodified_original':True,'inputs_reacquired':False,'original_calculation_rerun':False}
    (BASE/'repair-observed.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
