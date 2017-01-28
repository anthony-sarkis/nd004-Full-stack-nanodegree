
// BuildCat and countCat are helper functions
// used by showCat and showCatAll
// buildCatList builds a list of links for use by showCat

// Model View Controller layout

$(function(){

    var model = {
      
      init: function () {
        cats = [
          {
            Name: 'Whiskers',
            Img: 'a',
            Count: 0
          },
          {
            Name: 'Symba',
            Img: 'a',
            Count: 0
          },
          {
            Name: 'Kitty',
            Img: 'a',
            Count: 0
          }
              ]

        // push local storage if doesn't already exist
      if (!localStorage.cats) {
            localStorage.cats = JSON.stringify(cats);
        } 
      },        
      
      /* 

        Purpose: Updates Cats array of objects in local storage
        Input: Cat object with variable updates
        Returns: None.

      */
      updateCat: function(cat) {
        
        // get cats
        var catToBeUpdated = cat
        var Cats = model.getCatAll();
        var originalCat = model.getCat(catToBeUpdated);
        console.log("original cat", originalCat)

        // Update values in orginal cat
        // This is so it only updates the one field at a time
        originalCat.count = catToBeUpdated.count
        // console.log(originalCat)

        // Update cat
        for (key in Cats) {
          if (originalCat.Name == Cats[key].Name) {
              Cats[key] = originalCat
          }
        }

        localStorage.cats = JSON.stringify(Cats);
      },
      
      /* 

        Purpose: Get all cats
        Input: None.
        Returns: Cats, an array of cat objects.

      */
      getCatAll: function() {
        var Cats = JSON.parse(localStorage.cats);
        return Cats;
      },  

      /* 

        Purpose: Get single cat object.
        Input: Name of the cat, as a string. ie "Whiskers"
        Returns: Cat object from local storage.

      */
      getCat: function(catName) {

        var Cats = JSON.parse(localStorage.cats);
        for (aCat in Cats) {
          // get cat name from list
          if (Cats.hasOwnProperty(aCat)) {
            if (catName ==  Cats[aCat].Name) {
              cat = Cats[aCat]
              //console.log(cat)
            }
          };
        }
        return cat;
      }
    };
    

    var octopus = {
      
      /* 

        Purpose: Count number of times cat clicked.
        Input: Name of the cat, as a string. ie "Whiskers"
        Returns: None.

      */
      countCat: function(catName) {

        var $catOutput = $('#'+catName+'Output');
        $catOutput.text(catName);
        var $catName = $(catName);
        
        // get catCount object from storage
        // console.log(catName)
        var cat = model.getCat(catName);
        console.log("count cat =", cat.Name)
        $catOutput.text(catName + " " + cat.Count);

        $('#'+cat.Name).click(function(e) {

          console.log(catName, "Clicked")            
          cat.Count = cat.Count + 1
        
          $catOutput.text(catName + " " + cat.Count);

          model.updateCat({
                Name: cat.Name,
                Count: cat.Count
            });
        });
      },

      showCat: function() {
        
        cat = window.location.hash
        // remove #. Credit to http://stackoverflow.com/questions/3552944/
        var catIndex = cat.indexOf("#")
        var catName = catIndex != -1 ? cat.substring(catIndex+1) : "";


        console.log(cat)

        // get first cat
        var $cat = $(catName);
        var $catName = $(catName);
        
        console.log(catName)
        // get catCount object from storage
        // console.log(catName)
        var cat = model.getCat(catName);
        view.buildCat(catName);

        $(document).click(function(e) {

          if(true) {
            
            var cat = $(e.target).text();
            console.log(cat)

            view.buildCat(cat);
          };

        });

        octopus.countCat(catName);
      },

      init: function() {
        model.init()
        view.init()
      }
    };


    var view = {
      init: function() {
        view.buildCatList()
      },

        // Builds cat HTML tags
      buildCat: function(catName) {
          
          var cat = model.getCat(catName);
          //console.log("build cat =", cat.Name)

          $('<p>').attr('id', catName+"Output").appendTo('#cats').html('a');
          $('<img>').attr('src', catName+".jpg").attr('id', catName).appendTo('#cats');
      },

      // Builds cat list
      buildCatList: function() {
        // run through list of cats
        var Cats = model.getCatAll();

        for (cat in Cats) {
          // get cat name from list
          if (Cats.hasOwnProperty(cat)) {
            cat = Cats[cat]
            // console.log(cat.Name + "=" + cat.Count)
            // create list tag
            var li = $('<li>')
            // create link
            var node =  $('<a>').attr('href', "#"+cat.Name).html(cat.Name);
            // put link inside list and append to cat list div
            li.append(node).appendTo('#cat-list');
          }
        };
      }
    };

    octopus.init();
    octopus.showCat()

});