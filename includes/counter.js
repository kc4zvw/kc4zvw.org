// File: counter.js
//
// Speaking of Java, this particular script is (C) Copyright 2002 Jim Tucek
// If you wish to use my CountDown script, these comments must be left
// alone!  That is all.

// Visit www.jracademy.com/~jtucek/ for script information and a bit of help
// setting it up, or www.jracademy.com/~jtucek/email.html for contact
// information.

function start()
{
    setup(document.forms["form1"].time2.value,"form1");
    setup(document.forms["form2"].time2.value,"form2");
    setup(document.forms["form3"].time2.value,"form3");
    repeat();
}

function repeat()
{
    down("form1");
    down("form2");
    down("form3");
    setTimeout("repeat()", 1000);
}

function setup(day, box)
{
    today = (new Date()).getTime();
    the_day = (new Date(day)).getTime();
    time = (the_day - today);
    document.forms[box].time2.value=time;
}

function down(box)
{
    document.forms[box].time2.value = document.forms[box].time2.value - 1000;
    time = document.forms[box].time2.value;
    days = (time - (time % 86400000)) / 86400000;
    time = time - (days * 86400000);
    hours = (time - (time % 3600000)) / 3600000;
    time = time - (hours * 3600000);
    mins = (time - (time % 60000)) / 60000;
    time = time - (mins * 60000);
    secs = (time - (time % 1000)) / 1000;
    if (days == 1)
        out = "1 day and ";
    else
         out = days + " days and ";

    if (hours < 10) out = out + "0";
    out = out + hours + ":";
    if (mins < 10) out = out + "0";
    out = out + mins + ":";
    if (secs < 10) out = out + "0";
    out = out + secs;
    if (days + hours + mins + secs > 1)
        document.forms[box].time.value = out + " secs";
    else
        document.forms[box].time.value = ("It's here!");
}

// * End of File *
