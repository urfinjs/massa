#!/bin/bash

WAIT_ROLL_ACTIVATION=120  # seconds
DELAY_BETWEEN_CHECKS=30   # seconds
LOG_PATH="${HOME}/massa/massa_autorolls.log"

cd $HOME/massa/massa-client/

MASSA_WALLET=$(./massa-client wallet_info | grep Address | awk '{print $2}')
if [[ -z "$MASSA_WALLET" ]]; then
  echo "Can't find massa wallet address; exiting..."
  exit 1
else
  echo "Starting auto-buying rolls for $MASSA_WALLET"
fi


while true; do
  candidate=$(./massa-client wallet_info | grep "Candidate rolls" | awk '{print $3}')
  echo "active rolls: $candidate"

  if [[ ! -z "$candidate" ]]; then
    if (( "$candidate" < "1" )); then
      echo "less than 1 candidate rolls; buying rolls..."
      roll_purchase_result=$(./massa-client buy_rolls $MASSA_WALLET 1 0)
      echo $(date) $roll_purchase_result 2>&1 | tee -a $LOG_PATH
      echo "sleep $WAIT_ROLL_ACTIVATION sec"
      sleep $WAIT_ROLL_ACTIVATION
    fi
  fi

  sleep $DELAY_BETWEEN_CHECKS
done
