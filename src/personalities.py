from base64 import b64decode

NAUGHTY_WORDS = [b64decode(s) for s in [
    'bmlnZ2Vy',
    'ZmFnZ290',
    'dHJhbm55'
]]

MAX_TEXT = 210


def apply_personality(text, character):
    char = CHARACTERS[character.lower()]
    try:
        text.encode(char.encoding)
    except UnicodeEncodeError:
        return char.no_language()
    else:
        if any(word in text.lower() for word in NAUGHTY_WORDS):
            return char.naughty_word()
        elif len(text) > MAX_TEXT:
            return char.too_long()
        return None


class Character(object):
    encoding = 'cp1252'


class Skeleton(Character):
    encoding = 'ascii'


class Papyrus(Skeleton):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAADUklEQVR4nO2aQY6jOBSGP+axaYmRI/U5SmLRS1rmADlWX6ilOoCjqX0j5RyRHIUl6M0CE0gq9KQKnK7u4ZeqeNjWlx9D7GcTWLUqnhJ0IVKb/rUQCWBlvVXNYpyPeo0ra2WtrJX1q1kFiIIoXhwARpwXZxooAHFD/EhfQFsrReoBqx7ISuDw+R/XmxnHD/RFm/rvbZbB7rgBnsiQl/opd131OH6oL1qgFEx/LqEMwDZD/GhfSAVw7E6e6e6l8Azs0iGO7UtUX2eItQtBFcLtfqgcx/F8ZYAbVUgFtHk4y4fwDtYCOrPy8DfWM9sQbWELUvGlrxvHMX05uj7rlX0du9zT3dSKCq7iqL7k/C/owNYMn1x7qjYvyr52HEfx1efRRvWk6vpCUYcZZ9gFYH03bIgT18djTgxfVvWkJz+LE8OXqv74mL6c1cbP4kTqL1XNZ3Hi+GpEvZ/FiTc/ZhOt3sOap0uWTLR6D2ueJljSzeHqKPB4ADxeFKwfjXPRfI2eL6ONBcCqt+IB46ChEAdGG4+34sW/yp97ThxfXhsbMh2Pp6FL9BusOOj6zdOY13l9DF8Dy0A1SkLLcNxTZV1sNBTLxFZeDF9lC1CHsy5XZa8uK6kPXeExkQpq9W0S31cajlVtBlu9jumB60y+TSY3zGL0V31ziGh5qt213fK/WEvozPoEYTzoFNYUctU7V0uN26wFNKw7SuQ83HfJvDj4nuRD4za/9P4IX3wbF29NBSD7ilfFk10WZd9Xvar6vrDLVVWlG/AB8HjTYNU9clzF+p+2GssM/i84UXwZb4uTm8WJ8nxdj11zWAtoxKoWZM3Wb8CafSd/g2tcQOH7KP5cUmC0X+16uFx4/4QT/xrrXWr1pFolG204pDcb3cma6yvjR+GGit3x700CHEt5eTNrQV/tRaLTj/7qeGYqc55kLaCBVbpR8W7THZPSVK2989VpjHwVqnxzM+UrSex9rDj9VRu9OR+7u2eCOL5abu4DHPN3sOZrxCon9gEKuO8bGef5Ynd7+bWFp/uMRfJ1luhLC5vwrmOPHjd3sR7w+4nw7kP0/l9XLDsPTUwx4ZZOraxv66PmACtrZa2slbWyVtbKistKJ98SvFXth73G/wNr1Z+hfwGdZUfRmekUQAAAAABJRU5ErkJggg=="

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACvElEQVR4nO2aXW6jMBSFv8zNI5K7kUg8zCMVWUCk2dRsqFIW4FnAqEhZRyVH5RF05wHMT9rSVtiZdMbnocFgfRyuiTk4haSkeNqggUjt9lsgEkBifVZNMM6tXmNiJVZiJdbfZhUgCqI4sX6n4/mRwhXdcSjAUOCu6Atoa6XYOqBUB0b9U+HYfYilIAdEx+f+NWrfbt1Dm2Xw63wH5/stgEWq/nBuwSK0d5ur+qIF9oLxbaOQz7vUFvshVkhffWnOvnneAGR7f5Sjr11cX6L6MiHWdtY80A6bJ4A2j+4rg9moSPXivJyQSSu7zzlE95Xz4v7hOD8vtR0L+B0UTrF8bf2GpauZV3bvXuk+FLCi2m2K+cEY9ZLhT68nDqaimruCH2PrCNSxfPkcbVRV1fqdohYzS9ium9ql72LAjZNIx4nhq1RVVbeKE8OX3qwvK+ryVZw4vsobrdetjqMTdcU7fZc5kXyV6tasoVzlfVs6h2op/MyFw7FY0HjjWAJQqivFAcZCQyEWjDYOR8Nk8r3kxLrvm7Ifx85BF/QbSrHQ1U0a5A1bMcexasftff95ourDoLnMD4usQL66U/vHcB9FT2qzPfVTt/O8GeNqdF8+51RTW17n7RPQ8kHFqNelpU4tu9pOju0ugvXrrBAaWC3MXlL9i+Is7Mxbb7ICaGDVe2TIq10sFQsPm3zSe96K6WvI0ebndPfBVABymt1c8hvAnHldUdZ91U2f211WVRU7rkE4nu3ChB9nXqV0i70+woniy7iyeLarOHHu+4CsAJqwqoCs1foCrNUj+QWuMYD676O41ZxbvcY4rIzHwgZirdeYJ2Sp2+dYATSy9jYcK4R8pDJuLSeOL7nJdQBAVRfj6LucSN/t/XwhcxUrgNL/AyRWYiVWYiVWYiVWYiUWbP1PQavV3uw1/g+spH9DfwDXyR8lmYDjswAAAABJRU5ErkJggg=="

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAAD70lEQVR4nO2a0WrjRhSGP/X4piAYQ57DoEIvJ0iwt4a+VF9owbeFCQn0KkSQ5whMsKA3Gk4vRhpLjhu6a81uttWBYM2Z8Z9fGunMN7ZhjTXyRYEupBQ2Py2kBLBqfWn0i+l81HNctVatVWvV+u5a4jA92KFpsZjYoYAF04sz1H5IiX4TXxZxLzf3DguIKkBFrR5bxBEvNw7k8xYInWI3fmlfl9YhY+7vnXjfWwCDxaLgwY+25ehNvIR48Z7+m61D4XQo6ugciJv0luyGmQ5A867WV8TmUrIqm1cQDttoorDSAqGptQAom9lweYyvWa6XqI6E2P1RAeyf34y+27rx8G1nHl8l4P5xWHlbAdClTOfGB1banL6q4Q+ga0Bafp2MO6NtaUM1bR+y+XLEawYEQuegpU3DdsUehiIWrxUAD3C6lll8CWz5K6VDZRsmNeQwvMY7PlS2oXnm2QK8sDft0r7G/220P2rvYspD7THjDWSxHgOI9kCtbqj0PbGImJ6l69foq1ZVVX/Wd95+XyeHL1U1evwSH2918tT70E1r/HVa18eqdY1WuaDWdTHXkgW1rovLXAiAOIM4D4DBIO40RJzpTar/eX2VE34R1Tip0gKqDigx2oN4cRZe3hJSHl+dD5/c2AjbIq7iZQNs7hqg4vV2MHNAHt7Tuj5OZ22gnRWwGTEoRWqXQPkLKEU2X6NWE2CKVwxr9W5oFNvT2l2lnPG5fbXdua0YF1ITEtzN0jl8dW9KhLR7phUttpkR9J9tbl/8zDk+1G5uonbDwYHLkWff0SCzcl8WN0zQdGgTp3Yk2ya7L34/64n3TrDzNsDjrqo6J262o1zYV2Jl9WdcaJEn9UNNNxibXIjTo1M9q/d5uDB+CHKdThZfxtf26K7SyXJ/XSxUX6m1QEy02gW1ro4fQOvqmfwBznGBGJ5H8aeUDFto8Fg8llSr5uCq6kCesOroq+znWMLLxmhvGD976twu+Ujgqv62+OTFAbe1E5fHV8mTjSaokAdebze7006kAs7B9W58q4PCss3iK0xAJ1Qn0o9AERJEqE8gK60olNF0k+tebVw6nIDMaPC3dkhMwNU2oTjRKz4P37fVlmbeOXzuC5eLbtoN7AFCnnmkMyNPJDIFdiOANSmVugXiPD8Dh1zzGEi4l8gU5MLX32P3gyMaGrxnqhPN+PQlMkX4XFTnbzl1Q1olpM3m664o4n5wBxFH92Xa+UA9HiRwjc/lY0UA2+T/fsgiThWo+6PDqtbqzFtwFWctA0urRxd9Hv/97yfshZyZkHcmXl1A56MywKq1aq1aq9aqtWqtWnm1NuOPka6O8GHP8f+gtcZ/I/4G/Hph1jHxVvgAAAAASUVORK5CYII="


class Sans(Skeleton):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAADCklEQVR4nO2aQY6bMBSGv/RlackcoFLVA0Ri0SUSOcAcozfoAXqFXqXSbEdiNNlUalWkbHuFSI7E0pa7ACaTBGgChmZa/gUEY315YPz83gOYNWs8LfCBSG75JhAJYGZdKxuMc6vXOLNm1syaWTPrdbEkgwRAI9lAVl81sZIkHKuvmlh5EY7VV20sMUkiBiuZGczqoybW6g5QoBCQYay+amJtNuDWsIrU0sX5IFZf3Spr+acOd48Xs0a5Ru29zw7tci+ZGCxg/qpdBkhfnMhzNuz7sYKozDu098c3rNbFPjZs3lHb5b333jfkRhenS6PkQ3K0e6krfP8IdqnqMAvACiQLkJbj6M0Qzgh2+Vuz65WwVHOvXqxBKlkN81BXm3qP1npyu26ZlZOfnd23HnSzhqti1d5zXbeXa7YGsNhyINHd3n8EuxysKXDP7Qqp1wARIQYgls7odYxxXANQPK86q0hFlYWRingA4KFum8oupx4X5G4RZS3dimobT2VXFa8KxB92SN7S7a7afo0msqtirQ0AybpuF8Ou+rljxxaALZ0ubIT1UXtrsf7wjkG8mNKvihGjNWittXTMx1HWbe2fLF43BayXc8aYj0XCFRlGNyuEKlYM4nHd8+1CVhDVrB8BWSFU+/tPEVBEIVhBVOcd394vFou3JgQriOo6gMhP+DiMNUqc8wX41RDq9GEFUMXKiaFpNlZ11nM1vOYdwa+Kt4A//7NnuwxH/k3OXHBYv1o9Xw7xXBCSHrSJz5rGq5scWsVAasQkicZqrPagPRa0ZKk8ZWeLwzjr0H7N0e1SClBKlUHqIXYFFFlGU0gU0q4FtrFkmLpN+WxtV1uAvYnAvGOPfP+Qgft8Wke0k3yn4FrauzpMmvMV9yfuw60A2PRgXaXmUC+1kNrUJGK019qWfkJbwIoXn53VEaepm+QARZ4DxSFPKvfONY/yVN91JACSnbp708aZ9PlSp8tTe2o76f3S6OMekrVxpq7BXFr6nb8bmlkza2bNrJl1rZZlIhRA7mav8X9gzfo39Bt8UPQzIMG6IwAAAABJRU5ErkJggg=="

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAAC70lEQVR4nO2ZTWrbQBiGH+fzUjA6QKH0AAaFdimwDpBj9EC9SqDbwEC0KbRU4G2vEBiDlhqmC0m2lMiObc20cTvvQpo/PX41/2NBVFQ4LXCeSHZ544kEEFnnqvHGeavvGFmRFVmRFVnXxRINOaDoL62UApDHR30661JNsfJ8FDVzWJdqilXVUB5+xBZnsC7VIVYOYmhUjlKgHA0NKNEgWvT6b/ha3QGQIMLjtk0TEQGSLkfrwL6WE2ldG67SJKViuwWqJE0qqL/fAmTLKVt/dGwX7e2WrA8Ctqu3M1nnaKq+JnX/HrArADaspp4LUl/KOadHWWJ42sfUYL6otYyLBvRlgPEoK6nrvRVbD7LsoFHD+OrPHcq5FxU2IXOME8KXc84599rZSMwxToB2lNHtsKoTWF7Usfpxrz2wPKkBWLft6MwcTgBf7q35uhLW5PpyIWuWWpawXQCL9GC5nN1m0RjTh0L7gpSCLfs5XfSw1DjWSQ2uI5YPdSwLFRX2SMn9DjY9zvKijtVXVNGn57kYUEZpk7exPDdilAEMRmkwRmmld40aph1znrdWkkBGlnVzbYIkSZIBIGRtIOvu4Xx12nWwslwVYNMH7mooSwooVoVNAZLqHkhTywNpGtCXTUqyyhbP16GN7o1asMCmLVBI9xbDzU+I/aoAn56Qapy7zWAzSNPLDKDWyWKCFaAdC9cArin2OfIV1sNpAKTbOdqsn7oUg1ksgK+K8sEm6TCnqoCqGCXtNjpFf59geVIDoJxrmN6wDmssf5k94IQYj/XBEtkgrE9i+dDN7sfFYUcmOg3WgPVh9wOWF/WsHyeVrk5i+VEDkH9Uzrl2mbmYE+Lc8e3DYrF4Z3ywvKg/z4v8hM/zWEHWxy/Ar1c60KksD9rNqxlMjcYLWJ7UAEi7Ds35puy333f9yyIO2M5ihfvfZB4nyHfk9bxTbTBfHjhXckaOrMiKrMiKrMiKrMiKrMiarWV7EPIg+2bf8X9gRf0b+g28wvHN1utBXgAAAABJRU5ErkJggg=="

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACwUlEQVR4nO2ZMW7bMBSGP/d5JCAfoEsPYEBDRxYW0NXH6A16kV6lQA7AIFo6FNUBeoUCDKBRBDuITC1bTlKLNJKW/yBLj8Ln36T5/J4MRUX5tMInIrn1m0QkgML6Ww3JOC/1MxZWYRVWYRXW62KJAQ1QIWYM6XCIr2itr+5r5i0vZl2qOVbXz9/bnr04z7pU51hitRbLIMYClRE7rp9YseNCosVe19d2DyhQCAhAjVLjmFJKYQAwMXYtX20LroHtRq1d3QFfm20TPDfbRnoA6WPsWr6eVBeOJgHrjNZP3bC/PQm5ejzK0Xc/y3xV3nvzJy43YsQyABYqIzcP8Rv2o2OO8kkWXxbYHQx0HS334WJD18VwPDvNJzn6jsr76YRFPTvHpu07oi/vvfd+pjd6druUpR+SycuhzuT+R1hJFFgxQ5oErEQaAHbjOnq7hJPBl39pvl4JS83fdRFrkUbW6T4MaSuUiNMkJmb+odmV5l7M5OThEpDZjZvHVxfKhFEz5eih2vpR1nIFVsyeTYxr0DoUqVqLFas1aH93Z3bs3IdHWCl9OWjocdNBpWKmVWNtKgDGYKS7jq8wUf3hr07b1g3SQ9vS1E3bAj3IPT26yexrrAudul1VnVthN4eDjlCbujCTDqD7aI4nNpcvBOr3vzhdnrE2ncqc2RYZ1rGxAMfLI4ZQmyImxDQ7zlRlGearqwbWyrOaDHanpw5HY5hVht/tyt8N+GquYH0+J8d+7DVjjZ+AlUKBVYN4HHUCVhJF1veErBSK+f7zBug3KVhJFPuOb+9Wq9Vbm4KVRPE5gMgP+LSMlaXO+QL8nJQ6l7MSKLA6ali2G7PkVfED4Jf8p5w2r4bvl0M8PDwnuUz5npss42T5H3m3rKvN5isB55X0yIVVWIVVWIVVWIVVWIVVWIu1HhuhBHIv9jP+D6yif0O/AY4t3i1p7pDQAAAAAElFTkSuQmCC"


class Toriel(Character):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACuklEQVR4nO2ZT4rbMBSHv1TZDAhewCfoDQydTSHgQC/Uo/RIgnTZMgNzgJ5gQAZvCjKvCznxOBMnzUQKQ6vfRpb9/PlnyU9/EigqyqcFmojULz8kIgEU1qUKyTjv9R0Lq7AKq7AKq7BuxvIJWUc0xxKVE3cJIJ6DkCy+jOPlc9r2zI2r1wFZ1jlC9AaIAN4gD2CCCRIkiADIgwiYIEE83uiUk7sfu2eAO6gdtrIVFdVwqXaArahawK7Os673tVW18WhtHNDBPTDtrvu/Y6X0ZcHFo+/9Zn+2C0B74G7m28viqwOIfmw1Xu/3xy+SQo6cy+Xr+eum+7gGprl4arSYZSVRzEejXkMzJpgoiHExHxGMGkDMVsEEEVHRnPm48yUqqlt1s2EyJMVsA2YaJ/pn+s/zcRI/wJP9mtLXcijrp/4TT9Rzcd3v5aTM7WtkdZtuMx/XL6fladb1Glny7ZdLxUqh+N3rj6bR+uGKHwUyffempzeJWAk0shzYVKwUGvpxq6oql/Wjn3Jus15lGKxkfP5u8Ip1MQftewtfZ9erF7DepqEfvaqGZuxHD0ZNkGDiXCkShnqQWKoJU06m9np8PLhmV7aiutu1XRXrtmpbW1HZVd/Nsq7Wi+G7pj8W0R2eaKE9Ok3maK8NG+hemziQp+0CGH8rX/Bz0z6eDV/EFeyw41jNsa7XnmVN+2W3wJ+XTFY6foaVRDGpmmCcoPsniQ75KEADRkWMmiCYQBNrOcfVwddaAhpQ589En+Jk6EcHLJZcN0Wmby/xMcMaGvd2Tnpfjd/VxM8GnuWk9zXugy5cUUw4OcYJUcCc2KddwEqjACg1HtbU5p20FwQwikNUHXa6h76Mk2febhfXsrLMQx5gnYaVROX/2sIqrMIqrMIqrMIqrMIqrMLKy1ry9h3jVP27fcf/gVX0b+gPocLrAndQpvYAAAAASUVORK5CYII="

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACoElEQVR4nO2ZS4rcMBCGv456ExBUg0+QAwwYkmWD+wA5TA6UY+QADhPIZkIP5BwDMvRSprKQX9OP6YelYZjoX7Qfsr/+rbKsKhuystJpgUYitcsPkUgAmXWtfDTOW73GzMqszMqszMqs984SBYTw4w6ap3vkHOsWDSxTT/4BmmYGK4q6PEcI3gARwIFR48UbREHEeONBvPHGi4qAmHsv3qjxgZM6jrunsLQrW1B87PrOFrYAClvYouvN0hYUdmWL06z5vu5VbVhbm3rqsl9phsV+jJuUvix0dn61myNH7ny4243bTVPcBvrtJL52AMFPH5fnagsWAHbVFgct6Xw9fYNPa+DUWJRhvPbDdvd982w7xXg0qqo61pKi3XgUoArrxoOIUeOpjILZGi+kGY+9Lwm+6otPk/0db6MeOrA1g3Vcob+qB9SzdZeeZQ7KzkT9ZXT1+4pXFe3yBVYEjaw/bv0lFiuGQkD0gcqxnfFSIG4ch3CYsm4/z2OliWMNNhYrhro43m9VtzKNo7uWk6a/SijH/eKGZ5QTuMjlazxXG1jFYt2igXUHtOWkRRwSZkR8N0++oq/J4/GRu2lLQ8h4moYxQ301XxNWWe43Dj4vK0JS+Nqwgd2YNAPwo7/bjbuGFUMj6xEe9xq/hgwV7Op4BnGKNV8Dy/Jz1Sf4vf5eYOYYK4q6PMcbVdT1e0VFRYwHKhGjVOc5CXytxaMerd2Zo1/iJIhjDSyWzJsi4/eXuDDiKqr6dk58X5Xrt8SdPPAsJ76vsQ6SmzPDNPmEKGCuqNNeYMWRB5QSB2vKwzrnck50X0apEdUaa27+fJsov6dZzGUlmYccwDoOK4ry99rMyqzMyqzMyqzMyqzMyqzMSstacnvF+Fztm73G/4GV9T70D0X91oBGxeDeAAAAAElFTkSuQmCC"

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAADbElEQVR4nO2aX4rbSBDGf7PllwFBCXSAZQ8w4JB5CRjkA+xh9ig5TA4gmH1cGMMcICcYaBG9BFrUPrR6ZE8kj6yoJ5NEH9hqV7U+f+4/1dUtw4oV6XCFLcTUbv5YiAlg5boUfjGet/obV66Va+VauVauletX58qoQsFp/w6AOiC+0uuSCvovR2TsjvplrkXQ5TlK0Aaogt7fK4CaevFqgngQDzjxaqAWLOJVA0/qfmwegW0o1zVFVtT1NVkBWQGQFXUNdR0swTbG9f267syyUNpJBbd9nRpooB7sw7q3pdGVEYf6v+0eDn0dcQCNj6VjNL63JdHVAOyDwq5n4jTIcoC2iKVjtEWWx5pJdD3+c2j+2gEnXXMEHTKeWFPMRzFX+rLfS6rcmQCUqmKUYS5KnIclUHbz0cQCTwpdamp2Z9WRQ7OpFCnjRPtI++H0y5pLZLFsP2666/ahfc9DjFoAzdfN0A0DiDXTxIlm3+yPPe1UWU810+jSj5+rpbiWQBj39t/78sv2/jsOBRKNe2lpR3OIC7kWQdde9968vcH2agTp1qFRuIlcC2CMS40uMGmXnYYopdEX4UBdwvXxGQbXyHzYFz8m0XUDtNsTnzjx6puQvypenfoY3MWLVw+q4ulaNlF7HQ7PfFmeFRTXhOyUooan3DQrsoIiZq3fcC2pa7sdrPFslbyJhfr4epNK155buJ2wVH+KcmKeKi5a07TX9bt31YQb/u6uGnPXLI/WJLqyB+QwQdjDuDVFvC+9VIq5aFUDsW5vWAKlqpqqaufzYsEnpqaaKF/dqcc8VrkXap/jSdCPFXC1ASbnzuNcC8ED6sLsKimr+TzL6ypd/KRutOKLPMvr6vdBOjvTSZPnqAFysk+bzbUMPGBscbBjK2+kvSBsoyvUrCKT2Y9vl9XVb8bqq4m3uHzEkWQdcgC73lFGu3beOFNlNMS9yvNaF69RV7SMjcDXel4b81GeTlDFqz83/pbUdYUf3O+ry4Ea3J9A7fKu1JUH4F/lfwrHe4vxk/FpXHNwlqsT9O2p6gyuCzGF69mpaj5YaSLXVMzgcgtyncFYnBCvcHS+qiZeVWxMV5rz1ckYPpbmR//fZFTWDK7zuKy9xvONH9te505df7ZnrCvXyrVyrVy/E9eG+TvGU7Rv9jf+Dlwrfg38D7y3JSk51mATAAAAAElFTkSuQmCC"


class Undyne(Character):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACIUlEQVR42u2aQWrbQBSGv+R5YxgYga/QrUGQLlUk6AF6ptygB+gxfIAJCnRTsA/QZbeBEQhCYcR0YUtxUrowsZzX9r2NjQd//Pzzz2jeILCymq+uyGciDYvrM+oy1qmVzsYx741lLGMZy1j/CSu+8XM7vzyFeQ8eSftvR78DREmSJM3/3K4hn2KNW7mVW80/j2F0YvIKJI1HIL+dRiQkSc8dnD1fk2H9w94TVkMPQBnGoZKVW3VdR0d3KV3FGLJKwvPEvz/+RwewZs36Irrurnx/EHM/NFD8aS1KBDZs2FxEV0NJ4w6pPrRKUIyr0E/5cwVQUIxj8+oa4PMyfNzPVDdtCS886780Yxbj737OoeseeSf04UjDw/S5O855H/l0qX0154CknLdBSz806gLJdT5pc72QLt+2OZZadC2m2POhklunq9/OieAq+eaTFr+un54wbejLnqDDr4n1Xai4LUTbufAx3EHjltp0DU3TAD+05T457yNOgrLcf23LDfBTiV+Lp3mMDJQLbesRQF6zS8yi67A95Ffdap4/93XmZlvnnCtdud/BsgHoB1V+SQ6lbHNOMSjxa+q3XRupJd6oOn/hk0iq2UanSxdAqmqv5rx6xJLHodzpOhfuL0/aMivrO/a6Ksko1OXblDTqkiQRhbkfJO1QmHt8QuM8vppj9+TGMpaxjGUsYxnLWMYylrH+JtYCOdMLv4N5/6b9ttW/UL8AbCbNS//V+2IAAAAASUVORK5CYII="

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACz0lEQVR42u2aTYrbQBCFn1OGYUDwBD5AThAQJEuDdIBAThII5AS5wRwgx5gDKHggmwEbsp1lIKuBFhGEgRKVhSzHlj1/jNXqzHQthGnLzx+l7tKrloAYMYaLCexISs301RG5otZjQ4+mE3MftaJW1IpaUesFazmPXNZ3YVQAYJ/C3U41BFcOWO8PZ7f+JPXnc8xsK2MkQIpSBTRATBSgkjQaHVVsaJ8zgU7ReumqS4TcTMHWG9dwKQigao8udal7DaDa5xrKR6ddyuZSrofq8dfjt8lmkl80RTh1okAGJACAZDZ+/Zp2XRZwBghwcO6M1XeYlZDfZlb+q1+iZFtCuvUohhw5jRx+PW5x6TbXbpHdHHZGfHABYG6aHcTa46JHrkQW5g5yifa5RD1xKUCn+UKfojMIV0nNlwyGa6OV4WRVZTXKwPzXVdOc40sqofnCPwt8RJGchsbVFPMrAD8f6VEH55oDv7I9O9hWLrepEo53UA5xf8T3skqvgZuL/XMqIOV41zFDgqzjpCyUKm5dUx0oCpDo7pv++iFeylaVyJIZZknaep5q7X6qCrNkVlXeuARA9Qm2v6vZMbzpD/jgKoDPJUsAJz2mugM972a7eOwfV8BpAQB10/u+6Rboe0zaD0nqj6tGWbc9xqbj+FrsGq0foM/1uN4nN0sWhtzc287JLEXZOVWjkaIAclIMuS8/AaqIy5G7JBA/sa5X1RSQJr94ZMfopX4ldZOtAtxnKs7qy2D2v7aeD+VzsSfpDMTFhWqIXKLiguHa0mpEVyHOL+x0Qy6YfKGa3nmq4zh1YjfSYOrXrrF3VIBLEuBSlCTve+Ts5fm2IwHacn0k25Ex5teBeLd1DOI6/l9afPH5uq1kref4qnYTYFVfn+jkw307wl7fN+HDdXzmniNdx/vyJRpmvprpS6s5UStqRa2o9Vz9hBzphd8m5n7UfjvGc4i/tHMMoCAN99AAAAAASUVORK5CYII="

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAAClUlEQVR42u2aQYrbMBSGv1SBEBA8gw/QExQM2Q7EByjMhXqIHqDHmAO4ZKCbwgRm22W3AzI1lIDM68KR46TTDp2JHLfV21gG8eXnPenllxJIkSJezNAzkdr5qzPqSqw/DX82Tsp9YiVWYiVWYv1XLHcxXXrqwkSCpm4ggOiRUhdf1xr0N0nJukddj+1zVHWQMREQMV4ERMWLEy/SZUjMxosXBVHjwfhuXkSf0yeseQCw+T5HeQ15P6uwOXldQ13bHGxu88jrPvu2T9mVqfbaBvEmDE6KOShuFF0fZ7KkAuC2LWmbk4k3YWCOFmLjD+9RdJUUpiw4VPAk3oaBzY5OQfnh/Zy65oEPFe/tY5Xq4n6fnw/lcT+JtB+DrltM/frrYlih3cLP4PrQy7pn4zO4Bq6b3Zxmt/BzP4vWJyrM55V7JiJCnwi6wKz9M3XF7V+2LZ/JCD0lQr48yKZyV5M51/a6KlHv1U7uvF3AJ5MV+9Z6cf8V+gRf4ArXLqbmC79XbGG7nNR9Tre+RLVwT9XRjbzuvVRrdZXpdYkT1/tVZ3znyYwfWdfmzosKvhpkZqCr84oiY+nqWW1JU1f9PgifL0LvSC91Hmrzg+kKXqeuyW1e9+7vJ18WV5cB4KHtbzWHXqcOftWNvR/XyurO4yCse6P9+pIwFhEdaz92rC0sSyihfcSV2qw/q2VkY9axoWoa2PLrryH39Nk7wj25qt0owCrsRxUVBdYiRlnv6yjj9lXEG6MA9gWcSL8rqKEomKCuO+vcVHTND8Pyprhvp3j/teQdU9E1qKNopUxwfRlVPxldA1YLzRTrOLynnFIdX8xJ9+SJlViJlViJlViJlViJlViJ9Tex5pgz/eG3Tbm/6Hk7xb8QPwBVoArQY4IKGAAAAABJRU5ErkJggg=="


class Alphys(Character):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAABv0lEQVR42u1aQWrDMBCcVIYQMCiQB/QFgR56DMSP7gMM6b35SEAivhRkpgfHjWsCTZBULWX3FBsxGWZWq13bgIZGvliAiZD66ikhL8V6NEIyHNVesRRLsRRLsRTrb7Dc7L61k98ALEwowcv+urLeFNHezbWyH9cWxtp72qEsvCaCdScAwEs73tgA2PhCuXoVbGdaAHidLd2W4XUV7L1vbi19K7S33TzDLezU3nUhXt8U/O1UcqVq4fSPuxOOHh4Dxc49ipVkHrIcQto81F0uWmnz40UvJ0wvNACwaGoTZOllSbYkYZwQvQZehuSeZItaFK8UCZbl+UQDwFeoKSW/JljPn34ZVSry+BhIGOtE+WiAfrmO2Y15fKwB44Ddyh1F+bgneWCIOiFDpnMo8BB1dGfgZYZuYqisgniNfU5UZc1S78eCzyCEV/Xjyt8x3xZ6ptBKqhMAyXNcguV5r9AAq7HEivTRyPLRxmzFjD4CAA8hUOJ+3AK9rP4LhjzHOZmn3iO23OfKrwbTyVuMj5eeohXnI/ZxNmbjBSsy7xPg6LsTxVIsxVIsxVIsxVIsxUqNVcEk+uC3V+2Lzo8a/yG+AFyy3tkfdQtuAAAAAElFTkSuQmCC"

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACZklEQVR42u2aTYrbQBCFP6cMsxGUYQ4wVwgkm8CAfLAcJYcRzECWzlFaxJtAicpC1o+H0TgTu9VN0rWSQDw9qqrrvW4aSpSIFxv8Rkjd9sMNeRWs94bdDKfkvmAVrIJVsArWf4cV0uj2y9+qnr+LXcaJkS/NtY7hZa70ML6b2Nq8hjq6n9dMVb0Zeape7q9Y/mv68aM0AJ/zWI9Thz13+5zmxJiw6n5gqhPbXTJeI4W2zWd+ubuHs3mlMvW92Np9DwbqfeS2HzqeXprc9o+nfIXM8sUeoNtX0uSVL3V3F3fqXPLV8xJ3x92bK04FYvC6RYNF0cc90G6pPJf+mmE9/GrvrhoVcepo7shYSfVBmXSuQWFZkWLUUaC7AwnHNzUyyZz4aV7b6AUJIC6mJqiDypOpqYP66+41xnqs3f3Jba6QofepqlX//OkwuNagulYdG+AL33ntcHoobbv+ehQA2Xx9U7olrMlrC1D1Fgzg4+KX1W71fLWbzfj3he+O3/Yp5tdJiELw2fwSF1MFapCDuCo1UK+3Hme8mr/HicfrGumOs6/dX2qw1OdMkpVu9461uQ4nGi8xc/LqL4Cugy4T/7WdqeBxfMunv3B3g8fFz0Ka/qJemF5BAUKq81WeAfiRXR2p+0qO5zm9NqqriS151Hj52mBDs2vopr7XwQuGB6ANu3DJ5lisewrtZr4cZxuPNkEdl7CONvnTy051PV7d/eRPqx0pz1fPQt89v9a51yEmLg7UquLUyebqHyUtjW5fRYv17ueI5ZmvbpsuXwWrYBWsglWwbr1/lBtd+O1K7pP6iRL/QvwG8vsl3I5Qsk8AAAAASUVORK5CYII="

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACZklEQVR42u1ay4rbQBAspwVLQNAGfUC+IOBDjl5GH5pfWRA4xw3KjwRmwJeFEZXDSPb4sWSNpfGQTJ9GwpTKVd0z3bKBEiWWixU4E9JQfZqRV8G6NfxsOEX7glWwClbBKlgFKw2WPbuvenJpr6yS8NJctbfnWolXBVR2XsOqFw+oik/Bq8KlYPu3CkDdAAA2dYPGOQCb1wZwbryfLFePgm2lw/73dOWmxbfH1NBRsB9Di2E/XcmHcn7B2j489dSpeh0NT+M30Kt1shCvw6Oci3Lte3vlE+nmDpI8scmKFwLSC1VhQmUCMO/Vo5+flzJEbvPQlONdbvNjkMtYyUavwMuQpKe/R7EleClJ7khs8+IlJGHITnxWvECai50ih/cT7R5wFWrmUo8R1pc39/SRxLcJ93t6ehKyu3yoWrUArE6ngE/no0CGp6GVa1I4uPgUb1L6WKMVC2w/P0/Ng/jQr07qqGK8k4ZX6Fc3AH628SvgugnKTPo4h6ZunHN67MyW16vDHlvIr4jZ2Oy4E0cBfE14PgrZk1BDdkcfqQoIYRHyXse1TZH3VUgvbAAOEhwFgKEJfWrUrYb1GutkPrrVKlQlUP+tNbVJ96+x07GWkY9CQKhUAjCqQphUPka8etJaxhu+3oazEC/Ds6NbM+BlOFoZnTK3NT1L/d5hW0zJP9Vk9ej+HlB6sXfiLKOXvKzFe86CNadetID3mfXRkJOMz8fHARDt+8zm2jBC7l4Px2M2PkJIL+yy4wXD+1JsKV7Q+zLfl9/dC1bBKlgFq2AVrIJVsArWf4NVQWb6w+9QtH/oXFviX4g/LfIp026R2nkAAAAASUVORK5CYII="


class Asgore(Character):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAADIklEQVR42u2az2rcVhTGf+MzUAwXjkEPkE3Bq4IggW4G5G3BDxPwKg9RyDbQxwh0e4O7dLHB20A23RausKEEzuV0IWlGTmaM7Y40ougOSEjc+fg4f79zEcxrXsOtBb4npLw82iOvGeu5y/aGM9t+xpqxZqwZa8Z6GZZ0zcinxStI8yTESfXt6q7ho1Vq34rpeoe6Hqhvxz9bbXcT2veh2Oyp6wPZS9ZhJQ6ogqpuBFAS9BrExNTUVEeyV8hrMUyE+78B6FnsGMpIKEJB0X8/bm6v5Nvov4c3QH3YmvNHPtu6996Aeje7AerXOr76Ma8o/VDKaw/qWPbqHBceyz8dPx+7slX5pn7ppn6BSmzyEe2l73D52PIyoAT8SY1orDqRaTNQyS+lNUgfck9gUPlTpkmxkfxI5Ua00PCbxFzb8FL3mGyl7nFSvMQ9rCxdujMRXkdtW8x/yS3vnhT2Y56bVHdUkqRKTMqP6BXqkes4MV5Skljxmn6NbwqVQvqmdqXmOiSvZae7RJ1FfrZGHTi+iOruMWxeJxAXUxPUQUxNrOma6mpi6sPnI0D+LhfDSSgojqlrCAVFKBoFVNcUofjeooPwKn+QZblVDbaObS8/9R6H5yVn2fjKPzv33RuQJPGx/UMaSUf/DnK+e18ugEU44bzz8Si8jvn8iZP3OT6qbRS4HTUfA1Z5ss0xgHqbjwpU63z05llVnGqEulpyd+m6ony+GhyUVyxdXKwM0+IlxMrdU5Cp8Gp1jr8F4PTr7p3103N7f/1xkV5l5OZ4OTX9lVCPTEd/dQa6oV7ADVOx1war+g+z0HB+BHfb2vUOOXdsqQppEvZSuJNVdxywRSUfyl4h/pI/hvhg2lcTVxUTFxvbXgtsCeiP+Uv6dMGvZ2t7vXpmVbXlEPOQXQFX3tf32qzmfig/ymnJ64sHpzapd09j+/Gom9Pyb3x4cAzQKdJwAiz0MLyAn+XNy8XEYPNjFbnqFy11cVXx9mdjx1fve5Nyp510/Pr1+HcwTR7q5HiJba5T4jW9vj1jzVgz1ow1Y710rpU9ffCbZ9sfdH6c1/9h/QvSwDfJGOMO4AAAAABJRU5ErkJggg=="

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAAC3UlEQVR42u2asYobMRCGP2cM4UAwhn2AlGkX3Br22kAeJm3eIg8TSKtwKR1iSJsy7YEWG8KBlkmxu7bvLnZ8F+9aBKmxJLS/f2b0S/+sDbnlNlybYGdCaqYvzsgrYz21xbPh5NhnrIyVsTJWxnoelvSXkaXFy0k7EvzTHg/D8io3LR93XXbzagoQ9ACHceLlv3bebuW6+bo+6fHZoD5HtttKDFAFgkaJaoJEaPvtPlSVqFEVNGqQ2O/NAXyOa7ZmGA+bWwAKV9T1Fa7o+7R9XEHRrqhxRTs3hrYX0u62Gti0H312L3rmfGmu26QGgM2eoZUAm1vCHsF6p4cBzq/tF3d5atU5A2iK3ep2hskegO5GA8SrP7bcYy3qw3ps82BKB9Rjn4tqq8ygKka10yBVJ9cgUREDVbWh9NjxikAJ2MkXkY5QDzV0ClSa59IapH40CxChslOrSYnDxqvlVVnER9fyS6KubXmpmQ9xoWY+KV5i5hYx3JiRCK8X3bXY/JTvvD9524/13qRaU0mQKpBUHtElap5v/rAbvQgvKQksmO9x0h2vMD6vae+7RI1Jc8SNXmR/4dXMvNud56ZRg0YxUJMIEiWqjqtHgOZesOqaoobCzaCuXcE9Zzp8vKZ9p3wZp7dHl9bo6DWyXDeRO34dWbmJEi5Qu38CeXtsZVO4GUdDNgCvK358Zvah8U9zNoPr0RErC3HvNUClqqYqBlSdHk1s5HO1ZH1juqD8S5h0ZF6+NDGJpXtESw+PRvA5+MrMgpPjvlTiyD7H3gHw+u6RCqeHRyOcq5PwqkFWV9PU/FdAzZOO/+oDtKKewIpU4rXDqv6hFhouj2AWkWTymPjvtQprWfSvAxKKl/Nvmo/OJxeveanm5/Nk4tXXQ3EJLI3UeNm6ZF4lxwsLS5ZVTJCXCAnyqjxLNCTHC/7gVdPgRUq8MlbGylgZK2NlrEtiTZEz/eG3ybG/aD2U2//QfgPPUTTEyBwWYgAAAABJRU5ErkJggg=="

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAADDElEQVR42u2av4rkRhDGf3s1yUJDDegBHDo6EExkGOhLHflVnDryK/hhDpy2WcMlMrvg1MnBpYYWIzADLcqBpPm79p3vRqvGdIEaqUZ8+qjurvqqGShWbD67w26E1K9e3ZBXwfqvlm6GU2JfsApWwSpYBevzsGQqRpYXLyfDkxCuX4nL1W2/G/ion0hIAo0axzsD0IFj1GfZzlG3w2+jtntyo99V0NKOT227SLzksKzEAFVQlUQkqkoCoiRNghqoaZKkBpI0zRov1x/EMAG6P4HWVaOrG+NX3dO20LZUrmrbwfeSe3srAfyFs4Xu9OEwvhyvX/s38HTu685krcTjOGv+OnxwWvMntgboz3xufRxnjdeUttwzuy+OOWKJ/TjNiLdD/pKkpiZGBDVJqgyrzquK4UFMda79OPJKQA3YVSHST8e5+Tz2yJjv6T+X1ix1yCxCAm+X3aSkZeI11kdLhOQGfln0tQMvNQsxbdUsZMVLzNw2xQczMuH1aiyL/Qf5nR+ulv3S5yZ+h5coPpLVPKINaoHHkBkvqYls2Zz/5EHjcI361J8mtvMcMgsvajEz6mtlf3qdqmcd9OO86x5+ckD44ySfqoTDl4fqOMRH5SFpknidcV+i53MV9TEekz5VBWpXUbm1q15EF9a/9Ov6TJ4+022ceVpez85L3vQ/ynv+ulCk/2gtdIm38/FaTTc/r6m+uVSk/2Z9xYx6ddyPjial1BzbbVV5JKqOnawSYRjlUVVRHX+baT8e4vX1u+369WmfsQK6tFZQ7far76DbD293+4ourfar+etQze7BdHuZwBbP96E2MUm1y4uXELyZRSeZ6Rz7flhk+1x0zrh27+JXPfJ0v8pNf0XUAvnorylAT7R3V4cSC8briOW/oBeabx7h0ZqPVcUF5hG61X1+8VLYyXY6Dsgmf4EL3/ZvXcguXptaLWw22fVDqQEaIzdetqvZ+Ox4YbGh8SlDXiJkyMsHmqGxzosXfIlWnZUXOfEqWAWrYBWsglWwlj0HkBv94bcvsV+0Hyr2f7C/AUH6SNrI939yAAAAAElFTkSuQmCC"


class Napstablook(Character):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACG0lEQVR42u2aTYrbQBCFP095KSiDD5ArGLIdkA6Qw8wNcqaB2QY6J4gPkCsEWkSQTTeVhWzL9gQnjqVx2dNlsCQvHs/186qqERQrNp3NsJGQ8vxhRF4F61xLo+EU3xesW8Sqk8t6NLPoph4HXmpm5lAnVgDRXxzNLnPYRP7S/hK8+avu/ZW85b3ZhYGcJo6y/SEcBfbKulodlKUfvd+nowqSzh+AputpHVTQ/YBqydIDr11aCTxK8KITYmbB7KeZgSRQVfVQj0DTbGtgua3I/c9V4lhB3kW0bd3ofW0WUftmZn1uSbpuHOfDbXW4pbrQrwDrj/D0tXHSt/fcEhbQqBNeD7vu2ACZzt3eIZBfnO1DFUDmF7XTnS/44rUCQrf6vna41+Y1SO7z//82o6n6Y3g6ElfdfMWjETb+eaAdn1cAVgKfBplYePFXdeiqCBIlaepQBVVN/bMkVUmaJE7Ja0aaszn7zbJ4/vxl0wHiYhOo3A33vbXxQ3897Nvz0fuQbJW1bezVjPOqA7TQ6hvrl3BaKiJtl0DiW/KaER7/GnbyEqrF4Tw7Ka/WmjpwetDRU/vu6POqmplZpB7OJ9RAbDO11iCmKiZJkUTdP01+PqG2s3gBzns8Q16/g/94cX7VQ35R8uscrEzJr3vA6oq/ClbBcoO1Lv4qWAWrYN3UHK0jrGnlPauCdbtYlSteXYnjv1p53/de+lCxe7Df5Kfbf/rElu4AAAAASUVORK5CYII="

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACI0lEQVR42u2aTWrjQBCFv6S9bCiDL2KYbUA6wBwmh5sD9JwgPkCuMNBiBMNAi8pC1p+xnclYsitxlxZqvHg819+rahuyZVvOHtCZkJrV44y8MtZHLc2Gk32fsT4jVpFM1qOqRjP1OPASVVWDfWILEO3FUfUyhy3kL2lfwZq/itZfyVreq14YyGXi6LoPwkFgb9xX/aQs7fT7MR0RcOnjA9BymlaDh/oX+A0bC7z6tHLw5IKVPuFUNaj+VlVwCURELNQjUJZdDWy6ihw/N4mjh6aPaFWZ6feFakT0RVXb3HLptnFcDUc/3VJN9K8Au2/w/LM0otsjt4Q1lGKE12OvjiXQUJvbOxw0P4ztQx6g4Q+F0Z0v2OK1BUK9fd0Z3GubHbimzf//24yW0sfwfNBcu7l1zDHKSdbz8wrA1sH3oU2srfjLT1wlEVxySVK9n19bxRQhndLO+XV7v6OphP7uJLYzmIgfnYEoInIsjgvotus6a1XqZMaphE4BqmEEq+Tq/csxbhWV6/1Sp+Hs4nV5PRCepqXo++xvNsPZrzk6xS7Eq9KyCJwYdK49R0PaX31ppBjuJ0TBJaciQNGenQKFiNNjOpqW4rUnd8bkJvvQuyZXjOPhGH9Oueu/q1vNOWftvV1k9vwqhvy6BOcOf6No7uA73gNWnf2VsTKWGaxd9lfGylgZ67NgHexpMc/RGesOsbwpXnWO479a/r/vV9GhbF/B3gBLnN9yVVWBJAAAAABJRU5ErkJggg=="

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACCklEQVR42u2aW2obQRBFj93+bCiDNjKQfBpmFuDFeHFZQJsswLMAb8EwQxry00PlY56SEYnQjFSRuxr0hMtVVd16NIJs2bazO3QlpO7hfkVeGetUS6vhZN9nrP8Rq0wm9aiqjRk9zrxEVdVgnSgAGntxVD3PYRv5S/qnYM1fZe+vZC3vVc8M5DZxdOMH4SCwV66rfk+Wdur9ko4IuHT6ALRdT4vgIX6A37GzwGtKKwdPLlipE05Vg+ovVQWXQETEgh6Bqho1sBsVOZ6rxdFDN0W0bc3osYBIzfusgA9op3N5Xg/zS7+/pZrwV4D6G7y8Vkb69sIt4REqMcLrfuqOFdARze0dDrofxvYhD9Dxm9Lozhds8SqAEIv32uBe29Xguj7/TcWxCi+L4trI/Hiwv8nFeAWgcPAc7cXR7/UhEZJLInGYelxyCeRN5Pgku/78NexoKmG6O2lERGg8ItM7RN/k2GS2wfzlxsraVmERybafrJfjxPcr1S/HolS4BiAeRq29NK87wtPyO/8I0B3uH8KROXYjXq1WZfhcvuQqeoQ0XH1pQ7m4nyhFnFL2WwjloEf3U126RN4veA3kjN0zGceqv8BvPDu/yjm/yPl1ClZHzq9bwIrZXxkrY5nBqudp8G8n921VDefg5FzNWBlr1T2tyXrMWF8Qy5viFXMc/9Xy/31vpQ9luwX7A1Ct4u7SKvtgAAAAAElFTkSuQmCC"


class Mettaton(Character):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACkklEQVR42u2aTYrbQBCFP6e0GWgogQ+QTSCrAcFsDZ4D5Bi5R8gN5jDZBpRVNhO8yAFygkCJMYRAi85C/pFnZGcGJHWTdC1s1JjH02vp9at2Q65c09WCMBJSW7wakVfGemn50XCy9hkrY2WsjJWxMlYcLJUNgIlP8x7dMh1eqkCFF6+a0jxufwKwdMumaRLitZIagAbgOnZeXR8aEPGgNxuVgGGR86p8XIT69Fl3JVBG1ssB66M4slFVjafXgVcFoHWflwTW0Xl1jFYp9kM1fE2tf5RuKiXR/rGtE1u3r4AfNuo9joeldXK83gB8c0nqVd2kN493AF/eP/2BxeUlQPvh/vioeQDtsdLduq42o3/JCrDgqfvZ8FQtu6zgJOuQ3HdhXo6ZVbx6TE29hD2f3ZjO5qvtLSCfy9Nkv4QGlq48HZv5fRRcf4qaZHzi6u3tVY+mvZTaRL7qpOz7vetNqsbUq+K6SMZX9zmnghAerDr6lwRFgwZVCbLzL/GqGiTMl1drJASjGt4UeLRuzucTgGtvxe4GabH9O62J/B7WIRiDQefx3snwXspU/eMdyHD+aovL1xPq5fCKPJx5vuLl+1+hYGMtyfkETk3NuVT0OvASCaHW+/R4VX5NdbnfttnzF1Cv/cD7qIekqoaBcm7HdSpewwFZjz5q3fU8vHpYTXninerFi+9IdZlVTfylv53H5LXAF5zRaZ8PtVGgsdJed9/Des1zTqHZfVz3p/pyUpyD19YDJsYnoDgZjcqrXQILV/LuyWgZk5fuP74/GZ2zrx3INurFS1CFLrNq0CBedW5fPf9GPq/1iHPeREfEek49twPa/i5m5ZXPDWWsjJWxMtb/gVUgIx34bbP2Ufcncv0L9QeHTOC4WZ+LLwAAAABJRU5ErkJggg=="

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAAClElEQVR42u1aS4obMRQspwzBIHgNukIgK0MvshxoHyaXyDI3mAPkGNkGGiYwG4OPMCcYkBjDEHiNsuie/sWfDGO1m0RvY0ktF0VJKr3XNpAiRbxYIFwIqVq+uyCvhPXa0IvhJO0TVsJKWAkrYf2XWO76vKgy6IueZzkFL2NHAxZAdl29RLoESHZND1RxogyAKJUqIgJQOyVj89o/tgoBedkq6AFrMgDWWGO9b3S1U/G6Ydl1PjWfj/0ZHvBTrWPRFiA/q82fE21/n9PtdSJe/LoI5XDPv5xIeSmdulORVTYur+VLY7XBonBZs0qHQvrjMlXdkQOAlD3/EgIQ3oXav6gSRBgAEQYqCoZ6Xoy6o+VVM7oZeNghaeSYaPHqoRK4H/jFa2hFWkfWS8lDN9Kx3vBJ1PqxKg+8dzjWGz6J4xMrAA9upnnOQzk7Xh8AYG1mqVf+fn7reAug+vV5drwI4JnbXjZau5OEQWbqTrlIBF78AuDHgXzU+9Pf7+e1EXyVWwCO2vqqBFEqACcqgSpa35DN3alUQHjX3o6RfLXOuKqsr5NttLDeGwuLQY5qLIDcWB//PJLbvzPWwdKu4/vE6uNmdaQSc/Bdnw6+aTt8j+6rhtnI7xej1qLOIUzWG8mi65VjPbqIZdQaJTn7bxvpO0eMPCcHQnhyeVeGiFABCSIoqAIRKgoCYBBQAe6oHa84+WoJuuCQn5ttTuDEWUcjFd3tufn7ae8hbpAP/Gs2+QRv9/ecT/7V7C8DlV3xdH5/Ydr99RyW8GWFuekFGHnaOWPmolfLi9SilO38eOUhIL+ZHS+Uhb7pPMbiBXFvxEm/IyeshJWwElbCSlgJK2ElrISVsA7FErzQH36rpP1V30+k+BfiN+l/zl7xrUiZAAAAAElFTkSuQmCC"

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACOUlEQVR42u1aQYrbQBAspX0xDLRAX8g1MOCrwHrMfiQ/2AfsY+awxwTvAwI55rQwiwTLwojJYSytJHtCFnvkIem+uCWZouhWV9dgAxIS6aKAvxJSv/l0RV6C9dFwV8OR2guWYAmWYAnWf49lb7O32bEFOOQ4zcndaG9XL5OLWL5uHzmUBuSOxXSRPCGvzZl73Vu4qypUoXaned+tX6+aDPAc797Lqn3cjweQx74BKoAmMxfLk/Oir4U3GPoXPsthCk9zlCu9X9sGxd6Wf564qX6V6+iXBgA2E/3y5Jkpkp/qqkvDKzCql09VJE99HpryMgDlck4beFFoZTa8Fli9ycxPbAH8tJn6HDbZ8foMAN9VlvXSu/z6eA8Axd1FvjUFLwLQ+2/vu9kN/nTpY+dOlVTSPUQ1AMsOZvSGEV7Dg5F/Wv26B4AO1CwF15FjMmAm986IPDmAHLvE71ffAEA/8whHf6qqsNMH9xOcjjrjWxPNI5GyWerE9lezzVBXFZVzvee/ASiT10vjy+bsd7qHZnX9GsZOA963Vk/0K/hTJkeHMIHkB/0a53HiW9P4LwNyewsd86qLpvJavtCAvd/ZqKGYqykn53XEogZ6qV/zd+w5fpVyD4EOFq0xl+Ak4KXg1MG08/crA17kwdjZfHgN+7FQaAH1I7s99NoBT2Ry4TWea0m3B+g6t3MtYOr6onKl4gW2F+LI78iCJViCJViCJViCJViCJViCdS42oCv94beX2t/0vC3xL8Rvy6W4vgs3CPQAAAAASUVORK5CYII="


class Flowey(Character):
    def no_language(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACQUlEQVR42u1awYrbMBB97vioMob8Qq8FH3oMOB/Qn13YD/CyeyxsoN+xIFHDUhihHuQ4cZyUlFj2sNX4EBPB4+W90WjGDpAjR7ooEGZC8uWnGXllrH8NmQ0na5+xMlbGylgZK2Otg8XMOF4r8mIBiz696IGs7WyvVd+4HK/FeRWQEgD4rQTodwnEj7F37pb+K0kfXXcAQACALbWr+zjo5dj6cvuiRa8DL5AAror5BXe+Bx07div42LQGgIlDm3Nq9mNb135XEeGQWd3b2Ed3g5dz8upNBFoPoEU9TKka9DJPMbN8YXTV1ab3L0AXr94/UnMOlUN9isX0RddzgMY2Ag4U7sGZXy/sDd5DB+PVPTdhC5L7cFLwIgoh2FoNrwPW1gPYH09FkmmXyrE9s0v6GMBBhjIW++hJ/JVXEh9JLAB6tSe8mCSSG+4sCQkHgF+nuZjGx3duAfkyWjOb8zuzMRvnANQ/NkvNQ82vs+L19WIHEb/8ttQ5ZOA/Vxid2o90IZM6GeVaal5+50u4CtXJ0ndTYTI7+oN/BS+i11MJwBWnSz8vzruTm8T1/swZEmYKFAgABRIKAAcSEjQA07MsUif6wWMqj7mizVL1/spTCnS30krmI1/YYSRXlVxOr/10NU4ft84g/9d7K7L34iT6jUan9p6U5sROZ36BW535pXQ/orGK9DryaoNtNfpISn2sw7NKH82dhTVZ/xU05f2xVfDFR605GStjZayMlbEyVsZKi1WCZvrDr8/ar9rf5/gI8QeB6r+VdAtdOwAAAABJRU5ErkJggg=="

    def naughty_word(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAACfUlEQVR42u2aUWobMRCGP3f2ccMs5AA9QcHQ14T1AXLZQg+wIXksxNBzBCTsl4LE9GHtrBNvGie21iKVwEi2Vz+//xmNZgZDGWWkGzPsREix+nJCXgXrvSOcDKdoX7AKVsEqWAWrYJ0HSwIoAOpgu8ZNzksDupNa1JfblT+rXvJDnFv3cqhuFAtb7SSgIEEVVPs5La8ZoQLQxwrkTwX9pINW7utmrXjX7H7zPP9KkkfP1wACwJV0+w9+e9uiKXgtG7UQrwG4j4v9B3+CuOl4VVvvFoe45oXP6yDRDdTNsE/9JHq1XQ3UfdHmxwz2+yx1h7l29WtlYh3DGVQVQK1fgxgtiEkQS1139LzEnIVW7c6eu1A9tkGnqId6XtphZmbdAVWbTsLryb/wFxWHNAXWj1PGiTk33+uFHNSHmC5OeIjS0cB9Xn2A1rUPFkzsGJwEcXVZ42dYHbPrm+jKVuE4nBS8RALq5tn1c66imFvqm1HqX5E1hV6GWqDtPs4riR0lOEAe3MBrcycGVQ0SQMJ2FhPb5x1S5Kvi6tsFto7NM0n8kzR+5JMp8lVoVzZ22/jD648UvGriRbOTP8T1hl8APA7E9fPrtVoCXnERK3xDs3cbXm7M3Wers81r1PlT6HVbAX722tHTnbc6abx/aR/XZ6USxBQJ8DQHMRm5SUMiXvKeW0hJHCc+hqWjxkyjl7rD90jYVzdJngOwPHxXrKj+z/7Xjt+7Y3ES/cY6T+2jZOoTizz9C+3y9K9MzyOty0ivgVdnrsvRjpKpHed2l6Ud6yMDa7L8y3Ly+yEtiLPPGnMKVsEqWAWrYBWsgpUWq0JO9IffWLQ/a35fxmcYfwGeyu/xOiBssAAAAABJRU5ErkJggg=="

    def too_long(self):
        return "iVBORw0KGgoAAAANSUhEUgAAAlQAAACoAQAAAAAOLE3PAAAC50lEQVR42u1azWrbQBD+3PFRMAK9Qq8BQXN0kR8gD9OH6AP0VQq9BjY412JDrj32GhgRQS4jpoeVZFuK3SRoZbXsHmQxu3x8nr/9dhEQRxzhxgI2ElK9/DAir4j11qGj4UTfR6yIFbEiVsSaDEtmxEsuv2/zwbPlQwqwcfPOTMrGGnjfZgW/QlqUpf9NMiDJsEAWNo70nUQq7xhm7xFSsPcMwFtqWFfg7XRxZG0C1cYLzMzMADMEYNsyBIAkYHN+Htz8h3BxzCsAIADAilw7fQU0gbtuTRVwDVQKVArFY9g47lIA9WcAwH29bqd/ACQvVWOdAXWGZej8KmFm7r7L6WbcAEnaHZ3S43rl8P2rcFwBK39oa2sOwMNR65i+f5kUn+zJyNrMYiP1lUiGAmDaqM9/gMmBlJSULVTee15kYrCnYmPy7t4foh6TuxS0/ol6kcxr3y5c6fAFb7gUSKfZt/OkdvhKcztvmxiZ2266vL/0ebvhVYiZSbExzIsXoFbY1mF+vNhWPENeBZkUc7zPub3buaFoZQNYet1UABY+lrah9P0uB9Uv69PyJd06kS4kUrDknZWUlazxkHg173fN5inMB6uCxXFVE/LdXrkkGbJO4bRqHmW5fw5XheDlkNrtGu5cnHpRvOqvCsCLaikXS/rWBZJ6eqF6PFQQJD0tG8xfz+wA/biP43BfXuB49qa/KkyfKJ7ObUJ1NZDNDxPUI5kp2PaykIyZrOlfRgohBVA0T/NKtV0Vrt8XCk9ibvvQCDiB7nNkRKwR/UU6U3/NFauaKa9knrxqmqm/1u8GkZD1iGN1P9SkJy2+kqerx/KNlkC88vxQ2jOp9wopK8l5S0hezsEd6vq+Jj1tqauQvOivmvS0JWTe57Y5ynsyCIvXMsxnLTJ+3i+7t1+9u6+hJj1pSUPG8dl+D6cfXmUJ27+Ox1CTnrYEiGP83iRiRayIFbEiVsT6d7CWoJE++K2j7y+IFcf/Mf4AUyNTYR7lP3oAAAAASUVORK5CYII="


CHARACTERS = {
    name: globals()[name.title()]()
    for name in ['toriel', 'sans', 'papyrus', 'undyne', 'alphys', 'asgore',
                 'napstablook', 'mettaton', 'flowey']
}
