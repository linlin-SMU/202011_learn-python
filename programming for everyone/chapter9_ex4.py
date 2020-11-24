b = {'stephen.marquard@uct.ac.za': 58, 'louis@media.berkeley.edu': 48, 'zqian@umich.edu': 390, 'rjlowe@iupui.edu': 180, 'cwen@iupui.edu': 316, 'gsilver@umich.edu': 56, 'wagnermr@iupui.edu': 88, 'antranig@caret.cam.ac.uk': 36, 'gopal.ramasammycook@gmail.com': 50, 'david.horwitz@uct.ac.za': 134, 'ray@media.berkeley.edu': 64, 'mmmay@indiana.edu': 322, 'stuart.freeman@et.gatech.edu': 34, 'tnguyen@iupui.edu': 12, 'chmaurer@iupui.edu': 222, 'aaronz@vt.edu': 220, 'ian@caret.cam.ac.uk': 192, 'csev@umich.edu': 38, 'jimeng@umich.edu': 186, 'josrodri@iupui.edu': 56, 'knoop@umich.edu': 10, 'bkirschn@umich.edu': 54, 'dlhaines@umich.edu': 168, 'hu2@iupui.edu': 14, 'sgithens@caret.cam.ac.uk': 86, 'arwhyte@umich.edu': 54, 'gbhatnag@umich.edu': 6, 'gjthomas@iupui.edu': 88, 'a.fish@lancaster.ac.uk': 28, 'ajpoland@iupui.edu': 96, 'lance@indiana.edu': 16, 'ssmail@indiana.edu': 10, 'jlrenfro@ucdavis.edu': 2, 'nuno@ufp.pt': 56, 'zach.thomas@txstate.edu': 34, 'ktsao@stanford.edu': 24, 'ostermmg@whitman.edu': 34, 'john.ellis@rsmart.com': 16, 'jleasia@umich.edu': 4, 'ggolden@umich.edu': 16, 'thoppaymallika@fhda.edu': 2, 'kimsooil@bu.edu': 28, 'bahollad@indiana.edu': 8, 'jzaremba@unicon.net': 18, 'mbreuker@loi.nl': 18, 'colin.clark@utoronto.ca': 2}
big_name = None
big_value = 0
for name,value in b.items():
    print(name, value)
    if value > big_value:
        big_value = value
        big_name = name
    else:
        continue
print(value, name)
#??
