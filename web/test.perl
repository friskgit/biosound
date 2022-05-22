#!/usr/bin/perl
    
use strict;
use File::stat;
use Time::localtime;


print "Content-type:text/html\r\n\r\n";
opendir my $dir, "./audio/" or die "Cannot open directory: $!";
# opendir my $dir, "./" or die "Cannot open directory: $!";
my @files = grep { !/^\.+$/ } readdir $dir;
my @tokens;
my $hour;
my $min;
my $sec;

# Head
# Body

my @sorted_list =
    map  {$_->[0]}
    sort { $b->[1] cmp $a->[1] }
    map  { /([\d_]+)\.mp3$/ ? [$_,$1] : [$_, 0] }
         @files;

print @sorted_list;

# for my $i (@sorted_list) {
#     @tokens = split(/_/, $i);
#     $hour = substr(@tokens[1], 0, 2);
#     $min = substr(@tokens[1], 2, 2);
#     $sec = substr(@tokens[1], 4, 2);
# #    print @tokens[0] . ", at " . $hour . ":" . $min . ":" . $sec;
#     print "$i\n";
# }
closedir $dir;

1;
