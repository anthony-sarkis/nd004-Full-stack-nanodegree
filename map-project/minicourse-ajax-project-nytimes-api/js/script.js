
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
    // Built by LucyBot. www.lucybot.com
    var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    url += '?' + $.param({
      'api-key': "XXXXXXXXXXXXXXXXXXXXXXXXX",
      'q': address
    });

    $.ajax({
      url: url,
      method: 'GET',
    }).done(function(result) {

      $nytHeaderElem.text('New York Times Articles About ' + address);

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



    return false;
};

$('#form-container').submit(loadData);
