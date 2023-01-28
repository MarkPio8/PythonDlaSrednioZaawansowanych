from datetime import datetime

# START & END declaration

start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()

def CreateFunction(time = "m"):

    # This function crate function to choose in which measurement you want time
    sec = 60 if time == "m" else 3600 if time == "h" else 86400

    # Function below calculate delta time
    source = """
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
    """.format(sec)
    exec(source,globals())
    return f


# TEST
f_minutes = CreateFunction("m")
f_hours = CreateFunction("h")
f_days = CreateFunction("d")

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))