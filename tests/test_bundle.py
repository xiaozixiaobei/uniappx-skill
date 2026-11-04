"""Offline distribution checks. Behavioral cases live in scenarios.md."""
from pathlib import Path
import json
import re
import unittest
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    'uniappx-workflow', 'uniappx-foundation', 'uniappx-api', 'uniappx-ui',
    'uniappx-privacy', 'uniappx-quality', 'uniappx-build', 'uniappx-store-publish',
}
OFFICIAL = {
    'doc.dcloud.net.cn', 'uniapp.dcloud.net.cn', 'hx.dcloud.net.cn',
    'developer.apple.com', 'developer.huawei.com', 'dev.mi.com',
    'open.oppomobile.com', 'dev.vivo.com.cn', 'app.open.qq.com',
    'beian.miit.gov.cn',
}


class BundleTests(unittest.TestCase):
    def check_skill(self, name):
        folder = ROOT / 'skills' / name
        entry = folder / 'SKILL.md'
        self.assertTrue(entry.is_file(), f'Missing skill: {name}')
        text = entry.read_text()
        header = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        self.assertIsNotNone(header, f'Invalid frontmatter: {name}')
        self.assertRegex(header[1], rf'(?m)^name: {re.escape(name)}$')
        self.assertRegex(header[1], r'(?m)^description: .+')
        metadata = (folder / 'agents/openai.yaml').read_text()
        self.assertIn('$' + name, metadata)
        sources = folder / 'references/sources.json'
        self.assertTrue(sources.is_file())
        records = json.loads(sources.read_text())
        self.assertTrue(records)
        for record in records:
            self.assertIn(urlparse(record['url']).hostname, OFFICIAL)
            self.assertIn(record['status'], ('verified', 'entry-only', 'pending'))
            self.assertRegex(record['checked_on'], r'^\d{4}-\d{2}-\d{2}$')
            self.assertTrue(record['scope'])
            if record['status'] == 'verified':
                self.assertGreater(record['text_chars'], 500)
                self.assertRegex(record['sha256'], r'^[0-9a-f]{64}$')

    def test_exactly_eight_canonical_skills(self):
        found = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
        self.assertEqual(SKILLS, found)

    def test_all_local_markdown_links_resolve(self):
        files = list((ROOT / 'skills').rglob('*.md'))
        self.assertTrue(files)
        for file in files:
            for link in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', file.read_text()):
                if urlparse(link).scheme or link.startswith('#'):
                    continue
                target = file.parent / unquote(link.split('#')[0])
                self.assertTrue(target.exists(), f'{file}: broken link {link}')

    def test_workflow_reaches_every_stage(self):
        folder = ROOT / 'skills/uniappx-workflow'
        files = list(folder.rglob('*.md'))
        self.assertTrue(files)
        targets = set()
        for file in files:
            for link in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', file.read_text()):
                if urlparse(link).scheme:
                    continue
                target = (file.parent / unquote(link.split('#')[0])).resolve()
                if target.name == 'SKILL.md':
                    targets.add(target.parent.name)
        self.assertTrue(SKILLS - {'uniappx-workflow'} <= targets)

    def test_bundle_has_no_machine_specific_dependencies(self):
        for file in (ROOT / 'skills').rglob('*'):
            if file.is_file():
                text = file.read_text()
                self.assertNotRegex(text, r'/(?:Users|home)/[^/\s]+/', str(file))
                self.assertNotIn('uniappx-project-creator', text, str(file))
                self.assertNotIn('uniapp-native-app', text, str(file))

    def test_direct_stage_dependencies_are_resolvable(self):
        dependencies = {
            'uniappx-api': {'uniappx-privacy'},
            'uniappx-build': {'uniappx-quality'},
            'uniappx-store-publish': {'uniappx-build', 'uniappx-quality', 'uniappx-privacy'},
        }
        for name, required in dependencies.items():
            entry = ROOT / 'skills' / name / 'SKILL.md'
            text = entry.read_text()
            targets = set()
            for link in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
                if not urlparse(link).scheme:
                    target = (entry.parent / link).resolve()
                    if target.is_file() and target.name == 'SKILL.md':
                        targets.add(target.parent.name)
            self.assertTrue(required <= targets, f'{name}: unresolved direct-stage dependencies {required - targets}')

    def test_legacy_entry_reaches_canonical_router(self):
        entry = ROOT / 'SKILL.md'
        targets = []
        for link in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', entry.read_text()):
            if not urlparse(link).scheme:
                targets.append((ROOT / link).resolve())
        self.assertIn((ROOT / 'skills/uniappx-workflow/SKILL.md').resolve(), targets)


def skill_test(name):
    def test(self):
        self.check_skill(name)
    return test


for name in sorted(SKILLS):
    setattr(BundleTests, 'test_' + name.replace('-', '_'), skill_test(name))


if __name__ == '__main__':
    unittest.main()
