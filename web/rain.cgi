#!/usr/bin/perl
    
use strict;
use File::stat;
use Time::localtime;


print "Content-type:text/html\r\n\r\n";
opendir my $dir, "/home/h/henrikfr/www/rain/audio" or die "Cannot open directory: $!";
my @files = grep { !/^\.+$/ } readdir $dir;

# Head
print "<!DOCTYPE html>";
print "<html lang=\'en\'>";
print "<head>";
print "<meta charset=\'utf-8\' />";
print "<meta http-equiv=\'X-UA-Compatible\' content=\'IE=edge\' />";
print "<meta name=\'viewport\' content=\'width=device-width, initial-scale=1\' />";
print "<title>rain vaporprint</title>";
print "<link rel=\'stylesheet\' type=\'text/css\' href=\'../rain/vapour.css\' />";
print "</head>";

# Body
print "<body>";
print "<div id=\'app\'>";
print "<h1>rain vapour</h1>";
print "<p>rain vapour is a piece that has no beginning and no end.</p>";
print "<p>Listen to earlier versions of the tuning</p>";
print "</div>";


print "<div id=\'audio\'>";
for my $i (@files) {
#    $stat = (stat ($i))[9];
#    $d = ctime(stat($i))[9];
#    print "Last change:\t" . POSIX::strftime("%F", localtime($d)) . "\n";
    print "<p>";
    print "<audio controls>\n";
    print "<source src=\'../rain/audio/$i\' type=\'audio/mp3\'>";
    print "Your browser does not support the audio element.";
    print "</audio>";
    print "</p>";
}
print "<\div>";
closedir $dir;

1;
