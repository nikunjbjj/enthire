

all_zip_codes = open('data/usa_zip_codes_only', 'r').readlines()


for idx, zip_code in enumerate(all_zip_codes):

    if idx % 10 == 0:
        if idx != 0:
            f.close()
        f = open('data/url_lists_by_zipcode/num_%s' % str(int(idx / 10 + 1)), 'w')

    s = 'https://resumes.indeed.com/search?l=%s&lmd=all&q=software%%20engineer&radius=25&searchFields=jt\n' % zip_code.replace('\n', '')
    f.write(s)








