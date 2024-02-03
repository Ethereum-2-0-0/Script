function canRun() {
  var attack = User.getProperty("attack")
  if (!attack) {
    return true
  }

  var minutes = 2 * 1 - (Date.now() - attack) / 1000 / 60

  var wait_minutes = Math.floor(minutes)

  var wait_seconds = Math.floor((minutes - wait_minutes) * 60)

  if (wait_minutes > -1) {
  Bot.sendMessage(
  "You have already given Attack please wait "+wait_minutes+" Minutes"
    )
    return
  }
  return true
}

if (!canRun()) {
  return
}
User.setProperty("attack", Date.now(), "integer")

var url = "http://api.tuhin.my.id/putul.php?mail="+message+""

HTTP.get({
  url: url,
  success: "/success"
  })
