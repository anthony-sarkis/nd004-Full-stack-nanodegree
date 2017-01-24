
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    var streetStr = $('#street').val();
    var cityStr = $('#city').val();
    var address = streetStr + ', ' + cityStr;

    $greeting.text('So, you want to live at ' + address + '?');


    // load streetview
    var streetviewUrl = 'http://maps.googleapis.com/maps/api/streetview?size=600x400&location=' + address + '';
    $body.append('<img class="bgimg" src="' + streetviewUrl + '">');


    // load nytimes

    // NY TIMES data request
    // removed lucy bot as have customized it
    // update apiy key with correct key 

    var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    url += '?' + $.param({
      'api-key': "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
      'q': cityStr
    });

    $.ajax({
      url: url,
      method: 'GET',
    }).done(function(result) {

      $nytHeaderElem.text('New York Times Articles About ' + cityStr);
      console.log(result);
      articles = result.response.docs;

      for (var i = 0; i < articles.length; i++) {
        
        var x = articles[i];
        $nytElem.append('<ul id="nytimes-articles">'+ 
         '<a href="'+x.web_url+'">'
         + x.headline.main + '</a>'+
         '<p>' + x.snippet + '</p>'+
         '</li>');
      };


    }).fail(function(err) {

      $nytHeaderElem.text('New York Times Articles Could not be loaded.');
      throw err;

    });


    // wikipedia

    var wiki_url = "https://en.wikipedia.org/w/api.php";
    wiki_url += '?' + $.param({
      'action': "opensearch",
      'search': cityStr,
      'format': "json",
      'callback': "wikiCallback"
    });

    console.log(wiki_url);

    var wikiRequestTimeout = setTimeout(function() {
        $wikiElem.text('Wikipedia articles could not be loaded.');
    }, 4000);

    $.ajax({
      url: wiki_url,
      dataType: "jsonp",
      method: 'GET',
    }).done(function(result) {

      console.log(result);

      var articles = result[1];
      for (var i = 0; i < articles.length; i++) {
        
        articleString = articles[i]

        var wiki_url =  'https://en.wikipedia.org/wiki/'
        var this_url = wiki_url+articleString;

        $wikiElem.append(
        '<li id="wikipedia-links">'
        +'<a href="'+ this_url +'">'+articleString+
        '</a></li>');
      };

    clearTimeout(wikiRequestTimeout);

    });


    return false;
};

$('#form-container').submit(loadData);
