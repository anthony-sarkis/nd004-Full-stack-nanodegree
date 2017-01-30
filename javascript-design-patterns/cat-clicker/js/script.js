
/* 

  Purpose: Start program and run primary function, showCat
  Input: Model, Octopus, View
  Returns: Website with cat clicker

*/

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
        
        var cat = model.getCat(catName);
        console.log(cat.Count)

        var $catOutput = $("#"+catName+"Output");
        $catOutput.text(catName + " " + cat.Count);

        $("#"+catName+"Image").click(function(e) {

          console.log(catName, "Clicked")            
          cat.Count = cat.Count + 1
          $catOutput.text(catName + " " + cat.Count);

          model.updateCat({
                Name: cat.Name,
                Count: cat.Count
            });
        });
      },

      /* 

        Purpose: Show a cat and count it's clicks
        Input: Starts on click of a cat in cat list
        Returns: Cat and cat counter.

      */

      showCat: function() {
        
        $(document).click(function(e) {

          parantNodeId = e.target.parentNode.id
          if(parantNodeId == 'cat-list') {
            
            var cat = $(e.target).text();
            console.log(cat)

            view.renderCat(cat);
            octopus.countCat(cat);
          };
        });
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

      /* 

        Purpose: Render visual of cat
        Input: The cat's name catName
        Returns: Cat in html

      */

      renderCat: function(catName) {
          
          var cat = model.getCat(catName);
          
          // clear old cat
          $('#cats').find('p').first().remove();
          $('#cats').find('img').first().remove(); 

          $('<p>').attr('id', catName+"Output").appendTo('#cats').html('a');
          $('<img>').attr('src', catName+".jpg").attr('id', catName+"Image").appendTo('#cats');
      },

      /* 

        Purpose: Render visual of cat list.
        Input: Data from model.
        Returns: HTML cat list.

      */

      buildCatList: function() {
        // run through list of cats
        var Cats = model.getCatAll();

        for (cat in Cats) {
          // get cat name from list
          if (Cats.hasOwnProperty(cat)) {
            cat = Cats[cat]
            var li = $('<li>').attr('id', cat.Name).html(cat.Name)
            li.appendTo('#cat-list');
          }
        };
      }
    };

    octopus.init();
    octopus.showCat();

});