#!/usr/bin/perl
    
use strict;
use File::stat;

print "Content-type:text/html\r\n\r\n";
opendir my $dir, "/home/h/henrikfr/www/rain/audio" or die "Cannot open directory: $!";
# opendir my $dir, "./" or die "Cannot open directory: $!";
my @files = grep { !/^\.+$/ } readdir $dir;
my @tokens;
my $hour;
my $min;
my $sec;

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
print "<div id=\'app\' class=\'center\'>";
print "<h1>rain vapour</h1>";
print "<div class=\'center\'><p>by Henrik Frisk</p></div>";
print "<h2>Ulvh&auml;lls H&auml;llar, 2022</h2>";
print "<p>Listen to earlier versions of the tunings</p>";

print "<div id=\'audio\'>";
for my $i (@files) {
    @tokens = split(/_/, $i);
    $hour = substr(@tokens[1], 0, 2);
    $min = substr(@tokens[1], 2, 2);
    $sec = substr(@tokens[1], 4, 2);
    print "<p>";
    print @tokens[0] . " at " . $hour . ":" . $min . ":" . $sec;
    print "</p>";
    print "<audio controls>\n";
    print "<source src=\'../rain/audio/$i\' type=\'audio/mp3\'>";
    print "Your browser does not support the audio element.";
    print "</audio>";
    print "</p>";
}
print "<\div>";
print "</div>";
closedir $dir;

1;
