
// BuildCat and countCat are helper functions
// used by showCat and showCatAll
// buildCatList builds a list of links for use by showCat

// Model View Controller layout

$(function(){

    var model = {
      init: function () {
        cats = ['Whiskers', 'Symba', 'Kitty', 'Meowington']; 
      }
    };
    

    var octopus = {
      // Counter function
      countCat: function(catName) {

        var $catOutput = $('#'+catName+'Output');
        $catOutput.text(catName);
        var $catName = $(catName);
        var catCounter = 0;

        $('#'+catName).click(function(e) {

          console.log(e)
          console.log(catName, "Clicked")
          // updated counter to reflect new click
          catCounter = catCounter + 1
          console.log(catCounter)
          // output times clicked
          console.log($catOutput)
          $catOutput.text(catName + " " + catCounter);

        });
      },

      showCat: function() {
        // get cat
        cat = window.location.hash
        // remove #. Credit to http://stackoverflow.com/questions/3552944/
        var catIndex = cat.indexOf("#")
        var cat = catIndex != -1 ? cat.substring(catIndex+1) : "";
        console.log(cat)
        view.buildCat(cat);
        octopus.countCat(cat);
      },

      init: function() {
        model.init()
        view.init()
        octopus.showCat()
      }
    };


    var view = {
      init: function() {
        view.buildCatList()
      },

        // Builds cat HTML tags
      buildCat: function(catName) {

          $('<p>').attr('id', catName+"Output").appendTo('#cats').html('a');
          $('<img>').attr('src', catName+".jpg").attr('id', catName).appendTo('#cats');

      },

      // Builds cat list
      buildCatList: function() {
          // run through list of cats
          for (var i = 0; i < cats.length; i++) {
            // get cat name from list
            catName = cats.slice(i, i+1)
            // create list tag
            var li = $('<li>')
            // create link
            var node =  $('<a>').attr('href', "#"+catName).attr('onClick', "window.location.reload();").html(catName);
            // put link inside list and append to cat list div
            li.append(node).appendTo('#cat-list');
        };
      }
    };

    octopus.init();
});