dbus-monitor --session "type='signal',interface='com.ubuntu.Upstart0_6'" | \
(
  while true; do
    read X
    LOCK_SIG=`echo $X | grep "desktop-lock"`
    if [ -n "$LOCK_SIG" ]
    then
      python leetcode_web_view.py
    fi
  done
)
