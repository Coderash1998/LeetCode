class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        out = set()
        for i in emails:
            local,domain = i.split('@')
            local = local.split('+')[0]
            local = ''.join(local.split('.'))
            out.add(''.join([local,'@',domain]))
        return len(out)