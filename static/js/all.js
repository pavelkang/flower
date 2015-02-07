    var rose_id = -1;
    var comments_count = 0; 
    // We always assume that comments will only be
    // added and not deleted.


    function monitorCommentsOnPost(postid)
    {
      FB.api('/' + postid + '/comments', 'get', function(response) {
        if (!response || response.error) {
          console.log('Error getting comments');
          console.log('Response');
        } else {
          console.log('Got comments: ' + response.data);
          var n_comments_count = response.data.length;
          if (n_comments_count > comments_count) {
            for (var i = comments_count; i < n_comments_count; ++i) {
              var xmlhttp = new XMLHttpRequest();
              xmlhttp.onreadystatechange()=function()
              {
                if (xmlhttp.readyState==4 && xmlhttp.status==200) {
                  console.log('Successfully added comment: ' + response.data[i].message);
                } else {
                  console.log('Failed to added comment: ' + response.data[i].message);
                }
              }
              xmlhttp.open('POST', '/' + rose_id + '/addComment', true);
              xmlhttp.send('commment=' + response[i].message);
            }
          }
        }
      });
    }

    function postStatus() 
    {
      var xmlhttp = new XMLHttpRequest();
      xmlhttp.onreadystatechange=function()
      {
        if (xmlhttp.readyState==4 && xmlhttp.status==200) {
          rose_id = parseInt(xmlhttp.responseText, 10);
          var url = 'http://rosegram.herokuapp.com/' + String(rose_id);
          var content = 'Hey guys, I just created a birthday gift! It\'s live at: ' 
            + url +'. Go check it out or comment below to add your message as
            well!';
          FB.api('/me/feed', 'post', { message : content }, function(response) {
            if (!response || response.error) {
              console.log('Error posting message');
              console.log(response.error);
            } else {
              console.log('Post successful');
              var ids = response['id'].split('_');
              var userid = ids[0];
              var postid = ids[1];
              monitorCommentsOnPost(postid);
            }
          });
        }
      }
      xmlhttp.open('POST', '/createRose', true);
      xmlhttp.send();
    }
  