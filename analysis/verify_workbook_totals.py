#!/usr/bin/env python3
"""Recompute the key study and resource-reporting totals from the four
workbooks (Python standard library only).

Run from the analysis folder; the workbooks are read from ../workbooks:
    python verify_workbook_totals.py --output results/workbook_totals.json
It checks the study accounting of Section II, the counts of the citation search
(Supplementary Section S-II-F, records in ../search/citation_search_2026-11-07)
and the reporting indicators of Section VIII. The readout calculations of
Section IX have their own scripts.
"""
from pathlib import Path
from collections import Counter
import xml.etree.ElementTree as E
import zipfile,re,json,argparse,csv

N={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def read_xlsx(path):
 with zipfile.ZipFile(path) as z:
  ss=[]
  if 'xl/sharedStrings.xml' in z.namelist():ss=[''.join(e.itertext()) for e in E.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',N)]
  rel={e.attrib['Id']:e.attrib['Target'] for e in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))};out={}
  for sh in E.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet',N):
   target=rel[sh.attrib['{'+N['r']+'}id']];target=target.lstrip('/') if target.startswith('/') else 'xl/'+target;rows={}
   for row in E.fromstring(z.read(target)).findall('m:sheetData/m:row',N):
    vals={}
    for c in row.findall('m:c',N):
     v=c.find('m:v',N);inline=c.find('m:is',N)
     val=ss[int(v.text)] if c.attrib.get('t')=='s' and v is not None else ''.join(inline.itertext()) if inline is not None else v.text if v is not None else ''
     vals[re.sub('[0-9]','',c.attrib['r'])]=val
    rows[int(row.attrib['r'])]=vals
   out[sh.attrib['name']]=rows
  return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--folder',type=Path,default=Path(__file__).resolve().parent.parent/'workbooks');p.add_argument('--search',type=Path,default=Path(__file__).resolve().parent.parent/'search'/'citation_search_2026-11-07');p.add_argument('--output',type=Path);a=p.parse_args()
 audit=read_xlsx(a.folder/'Workbook_3_Extraction_and_resource_audit.xlsx')
 full=read_xlsx(a.folder/'Workbook_2_Full_text_assessment.xlsx')['Full-text assessment']
 rows=[d for n,d in audit['Audit'].items() if n>1 and d.get('C') in ['TIER1_SECURITY','TIER2_TRANSFER','TIER3_QUANTUM_INSPIRED'] and d.get('D')!='Report not retrieved; fields blank']
 assessed=[d for d in full.values() if d.get('D')=='Assessed'];missing=[d for d in full.values() if d.get('D')=='Unavailable']
 included=Counter(d['C'] for d in rows);quantum=[d for d in rows if d['C']!='TIER3_QUANTUM_INSPIRED'];tier1=[d for d in quantum if d['C']=='TIER1_SECURITY']
 stats={'included_studies':len(rows),'tier1':included['TIER1_SECURITY'],'tier2':included['TIER2_TRANSFER'],'tier3':included['TIER3_QUANTUM_INSPIRED'],'assessed_reports':len(assessed),'unretrieved_reports':len(missing),'fulltext_rows_marked_exclude':sum(d.get('Q')=='Exclude' for d in assessed),'quantum_denominator':len(quantum)}
 for key,col in [('qubits', 'AP'),('layers','AQ'),('shots','AR'),('execution_classifiable','AS'),('physical_hardware','AT'),('noise_stated','AU'),('explicitly_noiseless','AV'),('parameter_matched','AW')]:stats[key]=sum(d.get(col)=='Yes' for d in quantum)
 stats['tier1_qubits']=sum(d.get('AP')=='Yes' for d in tier1);stats['tier1_layers']=sum(d.get('AQ')=='Yes' for d in tier1);stats['tier1_shots']=sum(d.get('AR')=='Yes' for d in tier1)
 stats['not_auditable']=sum(d.get('BB','').startswith('Not auditable') for d in quantum)
 stats['evidence_levels']=dict(Counter(d.get('AE') or 'unassigned' for d in quantum))
 stats['tier3_classical']=sum(d.get('BF')=='Yes' for d in rows);stats['tier3_optical_CIM']=sum(d.get('BG')=='Yes' for d in rows);stats['tier3_both']=sum(d.get('BF')=='Yes' and d.get('BG')=='Yes' for d in rows)
 included_ids={d['A'] for d in rows};links={'R0268':'R0269','R0394':'R0164','R0497':'R0498','R0667':'R0659','R0152':'R0206','R0168':'R0167','R0251':'R0660','R0561':'R0167','R0715':'R0073'}
 assert {d['A'] for d in assessed if d.get('R')=='X8'}==set(links)
 stats['additional_included_reports']=sum(target in included_ids for target in links.values());stats['included_reports']=stats['included_studies']+stats['additional_included_reports']
 # X8 keeps report-to-study links even where the worksheet's row-level
 # decision says Exclude. Eight such companions describe included studies.
 linked_included=[d for d in assessed if d.get('R')=='X8' and links[d['A']] in included_ids]
 assert all(d.get('Q')=='Exclude' for d in linked_included)
 stats['linked_included_reports_marked_exclude']=len(linked_included)
 stats['fulltext_exclusions']=stats['fulltext_rows_marked_exclude']-len(linked_included)
 assert stats['included_reports']+stats['fulltext_exclusions']==stats['assessed_reports']
 expected={'included_studies':65,'tier1':15,'tier2':40,'tier3':10,'assessed_reports':120,'unretrieved_reports':13,'fulltext_exclusions':47,'fulltext_rows_marked_exclude':55,'linked_included_reports_marked_exclude':8,'quantum_denominator':55,'qubits':39,'layers':38,'shots':14,'execution_classifiable':19,'physical_hardware':2,'noise_stated':6,'explicitly_noiseless':7,'parameter_matched':4,'tier1_qubits':11,'tier1_layers':8,'tier1_shots':0,'not_auditable':6,'tier3_classical':9,'tier3_optical_CIM':2,'tier3_both':1,'additional_included_reports':8,'included_reports':73}
 for k,v in expected.items():assert stats[k]==v,(k,stats[k],v)
 assert stats['evidence_levels']=={'E1':7,'E2':5,'E3':5,'E4':2,'unassigned':36},stats['evidence_levels']
 decisions=Counter(d.get('Q') for d in assessed)
 assert decisions=={'T1':15,'T2':40,'T3':10,'Exclude':55},decisions
 assert all(not d.get('Q') for d in missing)
 # first-author confirmation of the initial extraction; the study added by the citation search (CIT-1) may still be pending
 confirmed=sorted(d['A'] for d in rows if d.get('BE')=='Confirmed');pending=sorted(d['A'] for d in rows if d.get('BE')=='Pending')
 assert len(confirmed)+len(pending)==stats['included_studies'] and set(pending)<={'CIT-1'},(len(confirmed),pending)
 stats['extraction_confirmed']=len(confirmed);stats['extraction_confirmation_pending']=pending
 check=read_xlsx(a.folder/'Workbook_4_Source_audit.xlsx')
 assert [check['Summary'][x]['B'] for x in [8,9,10]]==['120','54','1']
 # citation search: every retrieved row maps to one merged record, and the one included record is CIT-1 in Workbooks 2 and 3
 ret=list(csv.DictReader(open(a.search/'retrieved.csv',encoding='utf-8')));recs=list(csv.DictReader(open(a.search/'records.csv',encoding='utf-8')))
 assert {r['record'] for r in ret}=={r['record'] for r in recs} and len(recs)==len({r['record'] for r in recs})
 status=Counter(r['status'].split(' (')[0] if r['status'].startswith('Seed') else r['status'] for r in recs)
 screened=[r for r in recs if r['status']=='Screened by title and abstract'];dec=Counter(r['author_decision'] for r in screened)
 cs={'retrieved':len(ret),'from_reference_lists':sum(r['list']=='reference list' for r in ret),'citing_papers':sum(r['list']=='citing paper' for r in ret),'unique':len(recs),'duplicates':len(ret)-len(recs),
     'seeds':status['Seed'],'already_screened':status['Already screened in the review'],'after_cutoff':status['Published after the cutoff'],'screened':len(screened),
     'excluded':sum(v for k,v in dec.items() if k.startswith('Exclude')),'full_text':dec['Include T1 (analytical)'],'exclusion_codes':{k.split()[1]:v for k,v in sorted(dec.items()) if k.startswith('Exclude')}}
 assert cs['seeds']+cs['already_screened']+cs['after_cutoff']+cs['screened']==cs['unique'] and cs['excluded']+cs['full_text']==cs['screened'],cs
 assert {k:cs[k] for k in ['retrieved','from_reference_lists','citing_papers','unique','duplicates','seeds','already_screened','after_cutoff','screened','excluded','full_text']}=={'retrieved':614,'from_reference_lists':555,'citing_papers':59,'unique':568,'duplicates':46,'seeds':3,'already_screened':21,'after_cutoff':2,'screened':542,'excluded':541,'full_text':1},cs
 assert cs['exclusion_codes']=={'X1':2,'X10':4,'X4':453,'X5':10,'X6':70,'X9':2},cs['exclusion_codes']
 # the two passes as performed (column pass of both files)
 cs['passes']={}
 for ps in ['1','2']:
  rr=[r for r in recs if r['pass']==ps];sc=[r for r in rr if r['status']=='Screened by title and abstract']
  cs['passes'][ps]={'retrieved':sum(r['pass']==ps for r in ret),'new_unique':len(rr),'seeds_or_already_screened':sum(r['status'].startswith('Seed') or r['status']=='Already screened in the review' for r in rr),'after_cutoff':sum(r['status']=='Published after the cutoff' for r in rr),'screened':len(sc),'excluded':sum(r['author_decision'].startswith('Exclude') for r in sc),'full_text':sum(r['author_decision']=='Include T1 (analytical)' for r in sc)}
 assert cs['passes']=={'1':{'retrieved':529,'new_unique':494,'seeds_or_already_screened':22,'after_cutoff':0,'screened':472,'excluded':471,'full_text':1},'2':{'retrieved':85,'new_unique':74,'seeds_or_already_screened':2,'after_cutoff':2,'screened':70,'excluded':70,'full_text':0}},cs['passes']
 inc=[r for r in screened if r['author_decision']=='Include T1 (analytical)'][0];wb2=[d for d in full.values() if d.get('A')=='CIT-1'][0]
 assert inc['doi'].lower()==wb2.get('L','').lower() and wb2.get('Q')=='T1' and [d['C'] for d in rows if d['A']=='CIT-1']==['TIER1_SECURITY']
 result={'status':'PASS','key_totals':stats,'citation_search':cs,'scope':'Study accounting (Section II), citation-search counts (Supplementary Section S-II-F) and resource-reporting indicators (Section VIII), recomputed from Workbooks 2-4 and the citation-search records.'}
 txt=json.dumps(result,indent=2);print(txt)
 if a.output:a.output.write_text(txt+'\n')

if __name__=='__main__':main()
