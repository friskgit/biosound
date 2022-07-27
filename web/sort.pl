$DirName = "./audio/";

# Get a list of the files
opendir(DIR, $DirName);
@Files1 = readdir(DIR);
closedir(DIR);

# Loop thru each of these files
foreach $File (@Files1) {
	
	# Get information (including last modified date) about file
	@FileData = stat($DirName."/".$File);
	
	# Push this into a new array with date at front
	push(@Files, @FileData[9]."&&".$File);
	
}

# Sort this array
@Files = reverse(sort(@Files));

# Loop thru the files
foreach $File (@Files) {
	
	# Get the filename back from the string
	($Date,$FileName) = split(/\\&\\&/,$File);
	
	# Print the filename
	print "$File\n";
	
}
