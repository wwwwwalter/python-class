class CLanguage:
    def __call__(self, *args, **kwargs):
        print("CLanguage call")

clangs = CLanguage()
clangs("C语言中文网")