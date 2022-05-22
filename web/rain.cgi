#!/usr/bin/perl
    
use strict;
use File::stat;
use warnings;

sub get_sorted_files {
   my $path = shift;
   opendir my($dir), $path or die "can't opendir $path: $!";
   my %hash = map {$_ => (stat($_))[9] || undef} # avoid empty list
   map  { "$path$_" }
   grep { !/^\.+$/ }
   readdir $dir;
   closedir $dir;
   return %hash;
}

print "Content-type:text/html\r\n\r\n";

my %files = get_sorted_files("/home/h/henrikfr/www/rain/audio/");
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
print "<p>Listen to earlier versions of the tunings:</p>";

print "<div id=\'audio\'>";

foreach my $key (sort{$files{$b} <=> $files{$a}} keys %files) {
    @tokens = split(/_/, $key);
    $date = substr(@tokens[0], 32, 10);
    $hour = substr(@tokens[1], 0, 2);
    $min = substr(@tokens[1], 2, 2);
    $sec = substr(@tokens[1], 4, 2);
    print "<p>";
    print $date . " at " . $hour . ":" . $min . ":" . $sec;
    print "</p>";
    print "<audio controls>\n";
    print "<source src=\'../rain/audio/$key\' type=\'audio/mp3\'>";
    print "Your browser does not support the audio element.";
    print "</audio>";
    print "</p>";
    }

print "</div>";
print "</div>";

1;
