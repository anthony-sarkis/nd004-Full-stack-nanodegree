var initialCats = [
	{
		clickCount: 0,
		name: 'Tabby',
		imgSrc: 'https://drivecarma.ca/assets/img/product/logo/logo-red.png',
		imgAttribution: 'xyz',
		nicknames: ['Kitty', 'Kat', 'Whiskers']
	},
	{
		clickCount: 0,
		name: 'Kitty',
		imgSrc: 'https://drivecarma.ca/assets/img/product/logo/logo-red.png',
		imgAttribution: 'xyz',
		nicknames: ['Kitty', 'Kat', 'Whiskers']
	}
];


var Cat = function(data) {
	this.clickCount = ko.observable(data.clickCount);
	this.name = ko.observable(data.name);
	this.imgSrc = ko.observable(data.imgSrc);
	this.imgAttribution = ko.observable(data.imgAttribution);
	this.nicknames = ko.observable(data.nicknames);

	this.labelName = ko.observable(null);
	this.labelVisible = ko.computed(function() {
		
		if (this.clickCount() > 0) {
			this.labelName("Small");
		} 

		if (this.clickCount() > 1) {
			this.labelName("Medium");
		} 

		if (this.clickCount() > 2) {
			this.labelName("Large");
		}

		return this.labelName();

	}, this);

	this.headLine = ko.computed(function() {
		return this.name() + " " + this.clickCount()
	}, this);

}


var viewModel = function() {
	
	// self maps to viewModel
	var self = this;

	this.catList = ko.observableArray([]);

	initialCats.forEach(function(catItem) {
		self.catList.push( new Cat(catItem) );
	});

	this.currentCat = ko.observable( this.catList()[0] ) ;

	this.changeCat = function(ClickedCat) {
		self.currentCat(ClickedCat);
	}

	this.incrementCounter = function() {
		self.currentCat().clickCount(self.currentCat().clickCount() + 1);
	};
}


ko.applyBindings(new viewModel() );

