import requests

cookies = {
    'CTK': '1dan20bdhbi4m800',
    'RF': 'TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtZ4UZ2lYxAwQCQ-C8Xfdl6E=',
    'FD': 'ID=29687e69731d4874:IL=1557699505619:SG=cbf0479d3f057830c2004ece4f026fe7',
    '_ga': 'GA1.2.848374229.1557699509',
    '_gid': 'GA1.2.407743102.1557699509',
    '_gcl_au': '1.1.1622366009.1557699509',
    '_fbp': 'fb.1.1557699508702.382418713',
    'SURF': 'yPvO3GEyjn0uQWhj7ttjmCA4YNXhONbM',
    'gonetap': '0',
    'CSRF': 'Hcy093z4lJxpYDZbBMBxVPCcrxQJjVcT',
    'LC': 'co=US&hl=en',
    'INDEED_CSRF_TOKEN': 'frdFA3BmBa1c33AoG6kQB3gy2iAyTcB9',
    'IRF': '1qRi-3v0F_uf-yOkOwHemem4k5kxH8LlcrNj-SFeDD8=',
    'TS01d65e80': '0160a2beffbbe62cfbae483bdc6d1ccd59daffb8c83da0205d99b8dbbdb3cb2325eb292e32b61b552ac7ebe851871b0a9657e15784',
    'optimizelyEndUserId': 'oeu1557703304101r0.6147527100606782',
    '__ssid': '55da9d26bc0ecc103e013d78e870e37',
    'most_recent_searches': 'l=&lmd=all&q=software%20&searchFields=jt',
    '_gat_ga_tracker': '1',
    'RZT': '00.1557703379774.aiRr7j7THC4lYzEIapU2FHyz4P4Qtl4M1L2r+ASFlEk=',
    'TS01c598d3': '0160a2beff29884e4e7c67bdfdace7160100a193f3d552e2c31a3573c6643a317feec01d534417bc2c772b415d91de1b7ae7ccdb0ccbad59ecdfc21ae8fccf4cd28c069d7494810482337a42532f4d92d4c074ff05e6c3bfcde5a25e989e106e8f5d3c3f7a',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://resumes.indeed.com/search?l=&lmd=all&q=software%20&searchFields=jt',
    'authority': '6927552.fls.doubleclick.net',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'referer': 'https://resumes.indeed.com/search?l=&lmd=all&q=software%20&searchFields=jt',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'IDE=AHWqTUl0OFvai0yOku0AQtiHRQt9Tlsb3438ZbRUerbl0Agi85DHqaOwONX-7C0c',
    'Origin': 'https://www.google.com',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'X-RecaptchaV3ResponseToken': '03AOLTBLRQJkl3LJDNZ78qHsbx4KOpUQEDEK0dcpKdl_qNCgLGS47bYqdBPNL1r0MLWfbHrbC_xrvheSdNKtonrEfsERnTCl0hlztTdAbkuHc35cA9Fx8PyL77HDUMldaJvJ0w81qqu_-zA9jdc6rAwSet_3fyTe6Ch3A7bLhfuw3Oi7htKTlZ_mFBV7lMX3x6du9aPYJ9f8IyrS0DWqS4j3ds_PMSidzLD6CyY6GX7Tw1lXNHHU4Cg-09nmUunNjy4gbyoGR77BHkGQGzTcUseTN1V79IKzfGqXlf5pqiukab5u4uWVUe2oeGoTHqPn7YpO9A9rUVZd9I',
}

params = (
    ('l', ''),
    ('lmd', 'all'),
    ('q', 'software '),
    ('searchFields', 'jt'),
)

data = [
  ('$v', 'v1555968629716'),
  ('$v', 'v1555968629716'),
  ('reason', 'q'),
  ('reason', 'q'),
  ('c', '03AOLTBLQSsw0_k09mKTv-DHv0oSkeIhua2DMi0Rilbq6nxlI8nAPpekm1EqCHf1XRZGtZdnYAku33Vh9eQW7auyv6YgFrtvD1zZRlUDeM_PrL8FUR7Ued3Yo1WVpCGYmhLSW5u6ZLvWVxCsXh1iQ0r6SX4AZw9n-UxUe8ExL5ejCftBoj5Hy6Y_UWzDbGDTzgVpZsrNrLSlID_ZXI8rJEk3V4PvWb_E0vZG0_4Mqh42RC5ULuHqZcWmew0ETuuiXERLnVlR-0zJOoPgBmFlwKqak_Jyeb0E_M0HHxCXPpseOUAbjsN85YMS4v6yt5mciToqIFzFaAuPiXOSJQbKADr-qTTavOeWNxBdRfjbfqbUQa-O955jN6zd18wugft1Wlqwg3MaaUSm2AY6n5VIAimFGxt0vfl3buT4jKNOIfD-l9h95kSqoLxfsVrPOp08szddLYjiznGAvhzsUdpGxQNxwfhqZCSgmF9QMJk19X8AQxvl4UxMLdfwo'),
  ('c', '03AOLTBLQSsw0_k09mKTv-DHv0oSkeIhua2DMi0Rilbq6nxlI8nAPpekm1EqCHf1XRZGtZdnYAku33Vh9eQW7auyv6YgFrtvD1zZRlUDeM_PrL8FUR7Ued3Yo1WVpCGYmhLSW5u6ZLvWVxCsXh1iQ0r6SX4AZw9n-UxUe8ExL5ejCftBoj5Hy6Y_UWzDbGDTzgVpZsrNrLSlID_ZXI8rJEk3V4PvWb_E0vZG0_4Mqh42RC5ULuHqZcWmew0ETuuiXERLnVlR-0zJOoPgBmFlwKqak_Jyeb0E_M0HHxCXPpseOUAbjsN85YMS4v6yt5mciToqIFzFaAuPiXOSJQbKADr-qTTavOeWNxBdRfjbfqbUQa-O955jN6zd18wugft1Wlqwg3MaaUSm2AY6n5VIAimFGxt0vfl3buT4jKNOIfD-l9h95kSqoLxfsVrPOp08szddLYjiznGAvhzsUdpGxQNxwfhqZCSgmF9QMJk19X8AQxvl4UxMLdfwo'),
  ('k', '6Lf7EYoUAAAAAFAbKUrUD_Mku3P2rKzpOMttvGX0'),
  ('k', '6Lf7EYoUAAAAAFAbKUrUD_Mku3P2rKzpOMttvGX0'),
  ('co', 'aHR0cHM6Ly9yZXN1bWVzLmluZGVlZC5jb206NDQz'),
  ('co', 'aHR0cHM6Ly9yZXN1bWVzLmluZGVlZC5jb206NDQz'),
  ('hl', 'en'),
  ('hl', 'en'),
  ('size', 'invisible'),
  ('size', 'invisible'),
  ('sa', 'prepare_resume_search'),
  ('sa', 'resume_search'),
  ('bcr', '[-23494189,59721240,1989465762,1891015650,-1198249753,-2113216439,-2084469264]'),
  ('bcr', '[-23494189,59721240,1989465762,1891015650,-1198249753,-2113216439,-2084469264]'),
  ('chr', '[49,17,19]'),
  ('chr', '[49,17,19]'),
  ('vh', '1186305113'),
  ('vh', '268649148'),
  ('bg', '\\u21qK6gro9H1PPwQjmkYXZB2cmwb5vqxYYHAAAAVVcAAAE2nAgCWb4PeoImkHXhtivtNgnqMz-vdbkrj9jbv7EpBXJTnwjZFweL8zjXtVJofCpcq6UWdQHK-yxFR24lv856XrfAqE9QvH5jgxy18_2Nu48W21hPfwKkkcbkl593eTbH7WByHXoY9DX9wzo_b8wxFFQhwIV0OEsxLmx36_VcEWGL4A-k5YyzHvJIu_g0IHJmfDfMI4CZCJsbrPsJkua-O3eK4_JIXdW4IZX9vVcpWzUhzti81BdMs6uyKUZSpOYpi1VRKUXJ6ymHvAPkG1nPqtVeeoKct6XzgjA-Xh5HC20_8S-bNM3gJgpEryb796O5xBZbUFdRHlhAkTaYkqBTWMH0oXXMon_faSyidC0lnh5nxRgzzLzr6Qn7GiscqmVFeBQXJQeeG5n7tmBJB3mq0jVPqWcTLq7WCSy4iEX5IUvvzKfd4davseEGflplZDBoR3sUMWrRNsplE4ZIUi17sFT4C1_Mi2g7YQhduDs-Dr3Jlz-dsSrWkluZoZeCIySBAfZNfH-LnT1rGHfdntrIzsDTB50Xp2bYGIp-rbvqi5QnhIdrCv0nAkge2OLVyLLSdMExT-24jgvjbW-XnKL678fMhwctgEfZiFrbualbrGDZXkueQ5L3mQmZOlMd8ztLWKCSiYd_VPRWs0hR0bGNbm0K4a6DbIVq3VglGxXBy8rwLQnJ6dqGoOi-9K3bzUR-IjXkffrtFjVnAiw0oMm7kkzD96ZnBv-4z2XsQqVcE-7jhfCbwjsv7W0wdL056pVyEXhBOdRH_W1aAMNSBYij0F7IgRFr-Ll-CalNCU5g5z5i7zg1cZxKgIUJVwQwlXRSZBOA3am5LUDBf2_fGa3wN64jmEM_nKDotEEmQbiKO1ZcuEHtEYxhXfGJXDMrKoaABO__v4154sBNpQkkDNAad0-XoJcoil6Q8NzK1kt46wGEPeqph1wLehCSBc7GiCGThTRUxNhILpCEhHAUoyhYO3Q_F_JXpzHtYDptjcXvwrpKNHopmnWjobq3AHwePoCvmlQpeEcmNjqSjS9HRoX-w8TNJZqGImOhX3mGouex7RkvVLEhnD62t8X1jhFh9_xSSqzrSs2WgZIJZ7d4LbrPqfHCYQyHw2d0G_PBzA96-q8AfD-CVsNzxOz2uj4wl8YojpQG3G-6yyorpEofybLKmmEtCp2cLnUQL85yHL9KyZPQENlJs_qc_vlPWx-yrWaCPNfAm55Z8Ubw2539wDwwY9nv_Xp2RIICLqRQ8bfF7YCMYpcpf6sasIbe3r93l1IErLJrywgfrUsu0UI8jUJdfUDL3dBc-KXuAlcWtWqobR6xTmAH3VGfDRLnkNIrWTYfDOlY77OOrEEKEC-AAU4wsKNNwZBNT8bVk_RIZpGwCzYPznlgOEmo01mKI0qo-1LWJ3JdwthyjTYTJ6Ff_4_2fztrWzfWojgPD740z4LMDqUt4qZHkau_wzvNj-k6VSuI6fl-3JeLX1_jrcLmHtCbGBlGg1HgrkRHTT7xsGfFJHZin6T2hIy3Te6t_r7a0h_ymrycpzef7v5SredyaSq_gwE5Ji-4GfT3Jz6m15xoyIJkqrEsrjxrOYi3GyN25qcmeqgLLzEGLfUQK0FOP_2iHdYkPvEM38I5zosEBUprCuQ3rlDzzfGDv9nVQIoeZuOzbStbKrJBRv2jd7Cq1N9JIE2P6d5Muprg6nrxGyyKqySmEqKVkhfeFYqtjaGZusHHeBuR-rMGJFyu8jqBlL7R_2xXFkciDLzsoX39gpi6gVCrj7yI99-05XAsxRaZzP3xs2yysmj0fFA0PWtlxGVYVn5Emge03vl_yygAwCnTF3ssm_p21-Py9_bYog2bcYTg6xxexOFtjw4Dxjv_v2YkCnwtUFx3T5UBGYdKE-aPUPHJUvE_62Wt1UURiF74D9fk3cDPN4rZgvzfbrib0xkQzRSOL2DgH-xnPv_4JuA_DzY2UoOfoAYrqeXFyH841aT_bMSKJM3t9aI2KFOV_rdYoS1dH1IPg78ViDxOamL0dQSmisqoTmKQlE1gA2jP2wVDAnsYLh_gGqhMC-EVQTNElmfZFYEgxs7g10APk4QhXNMJEvHYGLCjnWLM-lGFkFCAdKJvTFgchMHbbb8lQnDuY5hvNo56ZN87afOfprzx6em9KCphtNEEAogCAwmdSbROQD3LstKL-IBTwXVvqweZUSN-mRKldCqH7lqs88U6LF3klFLNOMlFIgZ4vYuY-uE9C2dP1Qzxo4u-cTHbZhzbSVKKMTdCzETDPnB166EoGkgTQkAtFXgMsFH8rT1y9LzMTf1Pgt1pD3Y5vpnn1hu7MtkL_vCoCgv14aDVkJeA4BU5zhaYlsNsB85r3ND9Pz2FOYLykbi8oX30shSBN06QRborI_B5-BzElQ-VAZrgyWeK6aZlFrufGkTLTiX_qgumR3GOIgg_274FHTz8KmicvEioNQ4OIHbFXrm-vHWmRz2W06RXP4eNPmw0X78gDt0aM5Gw5nFZdDK2IjKFXipyOBvrE6FarXt54o30s92TlNigBh-TbdauLcV9Q72YBAGZiUwiYcmyUCRqOSNEaBdh26rlvS6sKDnaOuikQ9oSnw6f_lI4sbw5TdUQpfN7XI6q7UDXKhOhjr4c0N5xbd6K05jDQ8C82vd0m8v15NffhBFLpwf3AQ-8sscTgJqqjLY95IM0xZ0YRANka6MCUzo9XsJcFnWhRLi_cU00HIGEmD5OPcFR5w'),
  ('bg', '\\u21DQugCypH1PPwQjmkYXZB2cmwb5vqxYYHAAAAVVcAAAGLnAgdWb4PeoImkHXhtivtNgnqMz-vdbkrj9jbv7EpBXJTnwjZFweL8zjXtVJofCpcq6UWdQHK-yxFR24lv856XrfAqE9QvH5jgxy18_2Nu48W21hPfwKkkcbkl593eTbH7WByHXoY9DX9wzo_b8wxFFQhwIV0OEsxLmx36_VcEWGL4A-k5YyzHvJIu_g0IHJmfDfMI4CZCJsbrPsJkua-O3eK4_JIXdW4IZX9vVcpWzUhzti81BdMs6uyKUZSpOYpi1VRKUXJ6ymHvAPkG1nPqtVeeoKct6XzgjA-Xh5HC20_8S-bNM3gJgpEryb796O5xBZbUFdRHlhAkTaYkqBTWMH0oXXMon_faSyidC0lnh5nxRgzzLzr6Qn7GiscqmVFeBQXJQeeG5n7tmBJB3mq0jVPqWcTLq7WCSy4iEX5IUvvzKfd4davseEGflplZDBoR3sUMWrRNsplE4ZIUi17sFT4C1_Mi2g7YQhduDs-Dr3Jlz-dsSrWkluZoZeCIySBAfZNfH-LnT1rGHfdntrIzsDTB50Xp2bYGIp-rbvqi5QnhIdrCv0nAkge2OLVyLLSdMExT-24jgvjbW-XnKL678fMhwctgEfZiFrbualbrGDZXkueQ5L3mQmZOlMd8ztLWKCSiYd_VPRWs0hR0bGNbm0K4a6DbIVq3VglGxXBy8rwLQnJ6dqGoOi-9K3bzUR-IjXkffrtFjVnAiw0oMm7kkzD96ZnBv-4z2XsQqVcE-7jhfCbwjsv7W0wdL056pVyEXhBOdRH_W1aAMNSBYij0F7IgRFr-Ll-CalNCU5g5z5i7zg1cZxKgIUJVwQwlXRSZBOA3am5LUDBf2_fGa3wN64jmEM_nKDotEEmQbiKO1ZcuEHtEYxhXfGJXDMrKoaABO__v4154sBNpQkkDNAad0-XoJcoil6Q8NzK1kt46wGEPeqph1wLehCSBc7GiCGThTRUxNhILpCEhHAUoyhYO3Q_F_JXpzHtYDptjcXvwrpKNHopmnWjobq3AHwePoCvmlQpeEcmNjqSjS9HRoX-w8TNJZqGImOhX3mGouex7RkvVLEhnD62t8X1jhFh9_xSSqzrSs2WgZIJZ7d4LbrPqfHCYQyHw2d0G_PBzA96-q8AfD-CVsNzxOz2uj4wl8YojpQG3G-6yyorpEofybLKmmEtCp2cLnUQL85yHL9KyZPQENlJs_qc_vlPWx-yrWaCPNfAm55Z8Ubw2539wDwwY9nv_Xp2RIICLqRQ8bfF7YCMYpcpf6sasIbe3r93l1IErLJrywgfrUsu0UI8jUJdfUDL3dBc-KXuAlcWtWqobR6xTmAH3VGfDRLnkNIrWTYcDOlY77OOrFSvPseWtUCV4TuU_NJ47PxULcXuuC_Sbo6UG_SJQZO46VYrqaq_rPxrmdr8Sp8dSAkV_nNmZjRhEjAFiFWGfJEpMpk0WmaAQBU9ihPON0T39rEz1wZ0K5oe9Y3UfWKX86UA8iI5E7pl4MKKETnz3Ef2Sr6y91MMGElHI3IZCNGW4_V_Or8o-0cp5OFWsxmsKu0Dk9Lr5pOqXTXCEBgzScEYCywy6umbhQBZ4DsMcoIr7BvTb0bRNCZp7TXHZQMeZ1FROilrlakR1sCzQbxRAq03lpjanFnkmMGAdMsLTMvZ45GGq9GDp9bV7UPXWsQuoc7R5JU1parhsT23nPG84LZvdpsaK52s_tH1gsWDAsLvRYUgSoDtEs5aQ1Np-LRERB4kNaB9G0CcZiNnJkKFy97phZ-Pn0g_EGYE9mCHcpMS1uYOb6LC-AAwvfYZRV6n1wtZ_L3xFy1K9JS4qvpGplx7-tUWGBHNNhKUhzfu8VqGeDr5F4NGhWXiirMWVovpBQNPqffWhCScgSQROl4QRK0kRReg3Iy8fkUkseFtKIWKBiBtBOJ9CHbnFbw2CYlS8K7K5UOc0qlmsEUb42PIvApJWHw5VH5qqV3k5Jbw3YcIIBDDEepdbwnO2H7h0ExOkhNpeCbfPHa5SqwjMUvqUL5NPsgGD6MBMaTQv4IDO8wW8yxnKJgEr_uEmhNMavGoBLAtShMhfZixYdPgVeuxhDTRefOIUSPucVYwiItD652BEprgUCkpyTNUnKV1b271FSbROl9UNeE9DL8pQhyMRCb701CXM38LGruHDKj7hZxWfU0g9amgYTnrF3AOXOWI_qofWLcXmES87GTU8mJJJ46hOgeGM9MdUoRFt48lna9GG93CP5g5nf8pM-CLtuqg2UKNZiJ5H7E75owBBBpdDnnGIRnQeTxQxKBrnQ4Hr-7lpZXRZRbms_5J_nY6v9sx2xior4SyxpdUEb1T_K7kYN9MaiC5iSWBjlWaVb6DNxb3MWEG2Were7tYjqQJAAmuSVqCFOumnvH7Y9W9eJTgj3ltkGqM0RcOXQQ5hz4D6ABlCm1OQPabcxFqRXe2D7HPetczlc3o-wNTWVe1wEqXvss5ND4V8t42q8AVNYfU-aeSNIKYmiYLPT1kq_2VunXQ0jDagk1Uu4CMUQ5ciugYW9_fwM-lIFlhgIvSLNONCqFe9YlA1lVLZsmRFB952IPJRbQ9UMKVkEq4ocVN5FGeeUBNk2XHzjGrb3TbanPJJFXdbi45ycl0oAYOehC23fqfFyb9daUgugmsW-rM9B-HL0P_3PUaQGGH9ZZTqERDo7oAfylIdkycJ6T9VQCyyejYLFCle3avY5mWMAtLvA3iPaX9xZ5wbRcEp4tEKwLONcr6vXy0AAFEaTrSVfeiJWUguY5FNYWU8oC-Hw'),
  ('z', '05AHVohkY4I4fOorf5Gw6N8l-_1IDutoL5ZOR8u-9Iy7AxG6wQM1Sct4ERLudrUU0pmK_hdKreyKq2OamCBtsOEtqRN1h7tpwQFg-QgYZaIdpGodFZV7vBj842FNjaZ3NRMnAe8fAXVtcLL_usgZW2tSNHnr6aZW5WP51owJD-1ghG-6YTM_G4xRTSd8vXskFRe8_Ggf7H1DowlDBBvHFLfZUkY8wOR-l66vUG6FSsSL1kY57-8hfiNR3iPJLACR2IGPHNS5Sze_v69flcRE8o30WCS-eqNMaMlZguCiLC3sQ-Nc4moSKWLcOCGAT7OyLzukvcn6kI9pz3gYlw1cpOBbnU'),
  ('z', '05AHVohkafm-ykCMjwhV6qJGDEeDTTJWOYpOjMu9iP4KzKA-y6TWEFqXHW51WTJH1KV3p37Y3Uq1nr2eH0U03oWRaDIh_TXW-QdSOzSg2o3smuMAtl4TDkAFE20C-olFChdjZTW5y970rRKF_0dUeXaYY-LAmWSbfqlaA-2e-WefDsiNYHTg0cOj1qBN2LG4EF1blhAiS78YJMTwbU9QjQdRkinurwEI6pj2jkztkzS653C2SSjbLKQpMOB2yWoquY990ow877jBHi2BFqXe7ZOwj_SxUbuWgkFC8O8Zec_xiIkf2ZxH3JDaNCHz3_5mdoOvdNFLnMpx1MOFo45LUy1McXnChARvO-1Uttc97anJuBwwnEsmzEjaXspJZkgVt6StqrW-mNWn0dq7Ww4ueiN11TT67KuIczxORc42aNwA17yck0yQA72uw'),
]

response = requests.post('https://resumes.indeed.com/search', headers=headers, params=params, cookies=cookies, data=data)
try:
    resumes = response.json()
except:
    resumes = response.text
print(resumes)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://resumes.indeed.com/search?l=&lmd=all&q=software%20&searchFields=jt', headers=headers, cookies=cookies, data=data)
