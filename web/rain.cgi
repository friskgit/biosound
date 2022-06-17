#!/usr/bin/perl
    
use strict;
use File::stat;
use warnings;


print "Content-type:text/html\r\n\r\n";

my @files;
my @files_t;
my @filedata;
my $dirname = "/home/h/henrikfr/www/rain/audio/";
my @tokens;
my $date;
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
print "<title>rain will evaporate</title>";
print "<link rel=\'stylesheet\' type=\'text/css\' href=\'../rain/vapour.css\' />";
print "</head>";

# Body
print "<body>";
print "<div id=\'app\' class=\'center\'>";
print "<h1>rain will evaporate</h1>";
print "<p class='raise'><em>Henrik Frisk, 2022</em></p>";
print "<h2>Ulvh&auml;lls H&auml;llar, Str&auml;gn&auml;s</h2> <p class='small'>(<em><a href='https://goo.gl/maps/Miwiei1KqCx2BUAYA'>59.36309815334226, 17.042373214228594</a></em>)</p>";
print "<p>Listen to earlier versions of the tunings. These recordings are maid with fairly simply contact microphones that are sensitive to various kinds of interference heard as a hum in the background. Hence, these recordings are mainly for referencing how the tuning changes over time, and do not have the kind of fidelity one would expect from a recording.</p>";

print "<div id=\'audio\'>";


opendir my($dir), $dirname or die "Could not open directory [$dirname]: $!";
@files= map{s/\.[^.]+$//;$_}grep {/\.mp3$/} readdir $dir;
# @files = readdir $dir;
closedir($dir);

foreach my $file (@files_t) {
    # Get information (including last modified date) about file
    @filedata = stat($dirname."/".$file);
    # Push this into a new array with date at front
    push(@files, $filedata[9].$file);
}

@files = reverse(sort(@files));
		 
foreach my $key (@files) {
    @tokens = split(/_/, $key);
    $date = substr(@tokens[0], 0, 10);
    $hour = substr(@tokens[1], 0, 2);
    $min = substr(@tokens[1], 2, 2);
    $sec = substr(@tokens[1], 4, 2);
    print "<p>";
    print $date . " at " . $hour . ":" . $min . ":" . $sec;
    print "</p>";
    print "<audio controls>\n";
    print "<source src=\'../rain/audio/$key.mp3\' type=\'audio/mp3\'>";
    print "Your browser does not support the audio element.";
    print "</audio>";
    print "</p>";
    }

print "</div>";
print "</div>";

1;
