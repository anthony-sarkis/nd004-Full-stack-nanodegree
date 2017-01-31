
/* 
  Purpose: Start program and run primary function, showCat
  Input: Model, Octopus, View
  Returns: Website with cat clicker
*/

$(function(){

    var model = {
      init: function () {
        currentCat = null,
        cats = [
          {
            // TODO ADD ID  will also fix space handling

            Name: 'Whiskers',
            ImageURL: 'Whiskers.jpg',
            Count: 0
          },
          {
            Name: 'Symba',
            ImageURL: 'Symba.jpg',
            Count: 0
          },
          {
            Name: 'Kitty',
            ImageURL: 'Kitty.jpg',
            Count: 0
          },
          {
            Name: 'Kittya',
            ImageURL: 'Kitty.jpg',
            Count: 0
          }
              ]

      // push local storage if doesn't already exist
      if (!localStorage.cats) {
            localStorage.cats = JSON.stringify(cats);
            localStorage.currentCat = currentCat;
        } 
      },        
      

      /* 
        Purpose: Updates Cats array of objects in local storage
        Input: Cat object with variable updates
        Returns: None.
      */
      updateCat: function(cat) {
        
        var catToBeUpdated = cat
        var Cats = model.getCatAll();
        var originalCat = model.getCat(catToBeUpdated);
        // console.log("original cat", originalCat)

        originalCat.Count = Number(catToBeUpdated.Count)

        // Update cat
        for (key in Cats) {
          if (originalCat.Name == Cats[key].Name) {
              Cats[key] = originalCat
          }
        }

        localStorage.cats = JSON.stringify(Cats);
        localStorage.currentCat = cat.Name;
        console.log('local storage update', localStorage.currentCat)
      },

      /* 
        Purpose: Updates Cats array of objects in local storage
        Input: Cat object with variable updates
        Returns: None.
      */

      updateCatAll: function(cat) {
        
        console.log(cat)
        var Cats = model.getCatAll();
        var originalCat = model.getCat(cat);
        console.log("original cat", originalCat)
        cat.Count = Number(cat.Count)

        // Update cat
        for (key in Cats) {
          if (originalCat.Name == Cats[key].Name) {
              Cats[key] = cat
          }
        }

        localStorage.cats = JSON.stringify(Cats);
        localStorage.currentCat = cat.Name;
        console.log('local storage update', localStorage.currentCat)
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

        localStorage.currentCat = cat.Name;
        console.log('local storage update', cat.Name)

        return cat;
      },


      getCurrentCat: function() {
        var currentCat = localStorage.currentCat;
        console.log("cat from storage", currentCat)
        return currentCat;
      }
    };
    

    var octopus = {
      /*
        Purpose: Count number of times cat clicked.
        Input: Name of the cat, as a string. ie "Whiskers"
        Returns: None.
      */
      countCat: function() {
        
        console.log("Ran count cat start")

        var currentCat = model.getCurrentCat();
        var cat = model.getCat(currentCat);
        console.log(cat.Count)

        var $catOutput = $("#"+cat.Name+"Output");
        $catOutput.text(cat.Name + " " + cat.Count);

        $("#"+cat.Name+"Image").click(function(e) {

          console.log("Ran count cat click event")
          console.log(cat.Name, "Clicked")            
          cat.Count = cat.Count + 1
          $catOutput.text(cat.Name + " " + cat.Count);

          model.updateCat({
                Name: cat.Name,
                Count: cat.Count
            });
        });
      },


      /* 
        Purpose: Save cat
        Input: Form data from Admin
        Returns: Updated cat in local storage
      */
      saveCat: function(catName) {
        
        $('form').bind('submit', function (event) {
          console.log("Save Clicked");
          event.preventDefault(); // using this page stop being refreshing

          // credit http://stackoverflow.com/questions/169506/obtain-form-input-fields-using-jquery
          var result = { };

          $.each($('form').serializeArray(), function() {
              result[this.name] = this.value;
          });

          console.log(result);
          model.updateCatAll(result);

          view.runCats();

        });
      },


      /* 
        Purpose: Show a cat and count it's clicks
        Input: Starts on click of a cat in cat list
        Returns: Cat and cat counter.
      */
      showCat: function() {
        
        $('#cat-list').click(function(e) {

          parantNodeId = e.target.parentNode.id
          if(parantNodeId == 'cat-list') {
            
            var catName = $(e.target).text();
            var cat = model.getCat(catName);

            view.runCats();
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
      renderCat: function() {
        
        var currentCat = model.getCurrentCat();
        console.log(currentCat)  
        var cat = model.getCat(currentCat);
        console.log(cat) 
        // clear old cat
        // TO DO update logic to be use replaceWith function
        $('#cats').find('p').first().remove();
        $('#cats').find('img').first().remove();
        $('<p>').attr('id', cat.Name+"Output").appendTo('#cats').html('a');
        $('<img>').attr('src', cat.ImageURL).attr('id', cat.Name+"Image").appendTo('#cats');

      },

      /* 
        Purpose: Render Admin form
        Input: 
        Returns: 
      */
      renderAdmin: function() {
        
        var currentCat = model.getCurrentCat();
        var cat = model.getCat(currentCat); 
        var selectACat = 0;
        var fillForm = [];
        fillForm.push(cat.Name, cat.ImageURL, cat.Count);

        /* 
        Finds AdminForm ID, then for each input field, 
        if the inputType is not a submit type, it iterates over each
        It then replaces the value of the input tag where name is equal to name in loop,
        with the value attribute from the array specified above.
        */

        // credit http://stackoverflow.com/questions/5603117/jquery-create-object-from-form-fields
        $("#AdminForm").find("input, text").each(function() {
          var inputType = this.tagName.toUpperCase() === "INPUT" && this.type.toUpperCase();
          
          if (inputType !== "SUBMIT") {
              
              console.log(this.name)
              $('').replaceWith($("input[name='"+this.name+"']").attr('value', fillForm[selectACat]));
              selectACat++;

          }
        });

        octopus.saveCat(cat.Name);        
      },


      /* 
        Purpose: Render visual of cat list.
        Input: Data from model.
        Returns: HTML cat list.
      */
      buildCatList: function() {
        
        $('#cat-list').find('li').remove();

        // run through list of cats
        var Cats = model.getCatAll();

        for (cat in Cats) {
          // get cat name from list
          if (Cats.hasOwnProperty(cat)) {
            cat = Cats[cat]
            var li = $('<li>').attr('id', cat.Name).html(cat.Name)
            li.appendTo('#cat-list');
            
            // $('#cat-list').replaceWith($('<li>').attr('id', cat.Name).html(cat.Name));
          }
        };
      },

      // reveiwed with Yashwanth and ok
      // except to explore $(document) .ready
      runCats: function() {
          window.setTimeout(view.renderCat(),500);
          window.setTimeout(view.buildCatList(),500);
          window.setTimeout(octopus.countCat(),500);
          window.setTimeout(view.renderAdmin(),500);
      },

    };


    // place document .ready here to avoid using timeout statements
    octopus.init();
    octopus.showCat();
    view.runCats();

});