script="/home/pi/Documents/rain/biosound/player/cron/record_script.sh"
#  chmod +x $script
job="0 8,16 * * * $script > /home/pi/cron_log.log 2>&1"
echo "$job"
# remove the previous version of this cron job if it exists
crontab -l | grep -v $script | crontab -
crontab -l > cron_bkp
echo $job >> cron_bkp
crontab cron_bkp
rm cron_bkp
