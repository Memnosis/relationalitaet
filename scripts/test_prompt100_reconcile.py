#!/usr/bin/env python3
"""Synthetic-only tests. No real ChatGPT exports or private user data in CI."""
import json, subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPT=Path(__file__).with_name("prompt100_reconcile.py")
REQ=Path(__file__).resolve().parents[1]/"forschung/website/LETZTE_100_PROMPTS_QUELLEN_CROSSWALK_V1.json"
class TestProvenance(unittest.TestCase):
    def run_case(self,number=100,missing_time=False):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp)
            req=json.loads(REQ.read_text(encoding="utf-8"))["requirements"]
            mapping={}
            for i in range(number):
                text=req[i%len(req)]["summary"] if i<number-20 else "new unrelated instruction "+str(i)
                m={"author":{"role":"user"},"create_time":1762180000+i,"content":{"content_type":"text","parts":[text]}}
                if missing_time and i==0:m.pop("create_time")
                mapping["u"+str(i)]={"message":m}
            mapping["a"]={"message":{"author":{"role":"assistant"},"create_time":1762180000,"content":{"content_type":"text","parts":["do not count"]}}}
            chats=[{"id":"project","mapping":mapping},{"id":"unrelated","mapping":{"other":{"message":{"author":{"role":"user"},"create_time":1762185000,"content":{"content_type":"text","parts":["not part of project"]}}}}}]
            (d/"in.json").write_text(json.dumps(chats))
            (d/"allow.json").write_text(json.dumps(["project"]))
            cmd=[sys.executable,str(SCRIPT),"--export",str(d/"in.json"),"--allowlist",str(d/"allow.json"),"--requirements",str(REQ),"--private-out",str(d/"secret.json"),"--public-out",str(d/"public.json")]
            run=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            pub=json.loads((d/"public.json").read_text())
            priv=json.loads((d/"secret.json").read_text())
            self.assertNotIn("new unrelated instruction",json.dumps(pub))
            self.assertEqual(pub["verified_task_completions"],None)
            self.assertTrue(all(r["decision"]=="requires_manual_review" for r in priv["records"]))
            return pub,priv
    def test_100_synthetic_messages(self):
        pub,priv=self.run_case()
        self.assertEqual(pub["selected_messages"],100)
        self.assertTrue(pub["source_complete"])
        self.assertEqual(len(priv["records"]),100)
    def test_missing_timestamps_are_blockers(self):
        pub,priv=self.run_case(missing_time=True)
        self.assertFalse(pub["source_complete"])
        self.assertEqual(pub["source_issues"],1)
        self.assertEqual(len(priv["records"]),99)
    def test_no_unapproved_auto_completion(self):
        pub,priv=self.run_case(101)
        self.assertEqual(pub["selected_messages"],100)
        self.assertEqual(pub["human_reviewed_links"],0)
        self.assertTrue(all("original" in x for x in priv["records"]))
    def test_private_export_cannot_write_inside_public_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp)
            (d/"in.json").write_text("[]",encoding="utf-8")
            (d/"allow.json").write_text('["project"]',encoding="utf-8")
            forbidden=SCRIPT.parent/"test-secret-must-never-exist.json"
            cmd=[sys.executable,str(SCRIPT),"--export",str(d/"in.json"),"--allowlist",str(d/"allow.json"),"--requirements",str(REQ),"--private-out",str(forbidden),"--public-out",str(d/"aggregate.json")]
            result=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(result.returncode,2,result.stderr)
            self.assertIn("inside the public Git checkout",result.stderr)
            self.assertFalse(forbidden.exists())
    def test_public_export_cannot_write_inside_public_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp)
            (d/"in.json").write_text("[]",encoding="utf-8")
            (d/"allow.json").write_text('["project"]',encoding="utf-8")
            forbidden=SCRIPT.parent/"test-unreviewed-aggregate.json"
            cmd=[sys.executable,str(SCRIPT),"--export",str(d/"in.json"),"--allowlist",str(d/"allow.json"),"--requirements",str(REQ),"--private-out",str(d/"secret.json"),"--public-out",str(forbidden)]
            result=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(result.returncode,2,result.stderr)
            self.assertFalse(forbidden.exists())
if __name__=="__main__":unittest.main(verbosity=2)
