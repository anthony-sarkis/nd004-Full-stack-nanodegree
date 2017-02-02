var viewModel = function() {
	this.clickCount = ko.observable(0);
	this.name = ko.observable('Tabby');
	this.imgSrc = ko.observable('https://drivecarma.ca/assets/img/product/logo/logo-red.png');
	this.imgAttribution = ko.observable('https://xyz');

	this.incrementCounter = function() {
		this.clickCount(this.clickCount() + 1);
	};

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

ko.applyBindings(new viewModel() );

