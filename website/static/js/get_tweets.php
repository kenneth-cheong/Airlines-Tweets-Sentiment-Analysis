<?php
session_start();
require_once("../static/js/twitteroauth.php"); //Path to twitteroauth library
 
$twitteruser = "clar_ken";
$notweets = 30;
$consumerkey = "kfsUbDHgk2lsHZLACtpE5dM1g";
$consumersecret = "h5YKVUS9fhe1xRRUxHrttlIznVtvMlyPmvksOvPjcPt6wk236y";
$accesstoken = "226574436-2PI0j4sIYc3UQCEWchTjiWHqpgmtiwdmBuP4peI6";
$accesstokensecret = "4PckPJs5EHjdFG8z1kAUYFERlMjf8luVnudt03wgVXjE7";
 
function getConnectionWithAccessToken($cons_key, $cons_secret, $oauth_token, $oauth_token_secret) {
  $connection = new TwitterOAuth($cons_key, $cons_secret, $oauth_token, $oauth_token_secret);
  return $connection;
}
 
$connection = getConnectionWithAccessToken($consumerkey, $consumersecret, $accesstoken, $accesstokensecret);

$tweets = $connection->get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=".$twitteruser."&count=".$notweets);
 
echo json_encode($tweets);
?>