

function init() {

window.onload = function(){

    var w1 = new Timer("t1", "s1");
    document.getElementById("s1").onclick= function(){
      w1.start();
    }
    document.getElementById("r1").onclick = function(){
      w1.reset();
    }


    var w2 = new Timer("t2", "s2");
    document.getElementById("s2").onclick= function(){
      w2.start();
    }
    document.getElementById("r2").onclick = function(){
      w2.reset();
    }


    var w3 = new Timer("t3", "s3");
    document.getElementById("s3").onclick= function(){
      w3.start();
    }
    document.getElementById("r3").onclick = function(){
      w3.reset();
    }


    var w4 = new Timer("t4", "s4");
    document.getElementById("s4").onclick= function(){
      w4.start();
    }
    document.getElementById("r4").onclick = function(){
      w4.reset();
    }

    var w5 = new Timer("t5", "s5");
    document.getElementById("s5").onclick= function(){
      w5.start();
    }
    document.getElementById("r5").onclick = function(){
      w5.reset();
    }

    var w6 = new Timer("t6", "s6");
    document.getElementById("s6").onclick= function(){
      w6.start();
    }
    document.getElementById("r6").onclick = function(){
      w6.reset();
    }

    document.getElementById("moveAllBtn").onclick = function(){

        if (document.getElementById("moveAllBtn").value == 'START') {
          w1.status = 0;
          w2.status = 0;
          w3.status = 0;
          w4.status = 0;
          w5.status = 0;
          w6.status = 0;

        } else {
          w1.status = 1;
          w2.status = 1;
          w3.status = 1;
          w4.status = 1;
          w5.status = 1;
          w6.status = 1;

        }

        w1.start();
        w2.start();
        w3.start();
        w4.start();
        w5.start();
        w6.start();

      }
    }

}

function Timer(timerLabelId, startBtnId) {
			this.status = 0;
			this.time = 0;
			this.timerLabel = document.getElementById(timerLabelId);
			this.startBtn = document.getElementById(startBtnId);
      this.bg = document.getElementById(timerLabelId + "bg");
		}

Timer.prototype.start = function() {

			if (this.status == 0) {
				this.status = 1;
				this.startBtn.value = "STOP";
				this.count();

			} else {
				this.status = 0;
				this.startBtn.value = "START";

			}
		}

Timer.prototype.count = function() {

		if (this.status == 1) {
			var that = this;
      setTimeout(function(){
				that.time++;
				that.timerLabel.innerHTML = getTime(that.time);
				that.count();
			}, 10);
			document.getElementById("moveAllBtn").value = 'STOP';

      // 100 = 1 second
      if(that.time > 400) {
        that.bg.style.backgroundColor = "red";
        that.timerLabel.style.color = "white";
      }

      else if (that.time > 200) {
        that.bg.style.backgroundColor = "yellow";
        that.timerLabel.style.color = "black";
      }

		} else {
			document.getElementById("moveAllBtn").value = 'START';
		}
	}

Timer.prototype.reset = function() {
		this.status = 0;
		this.time = 0;
		this.startBtn.value = "START";
		this.timerLabel.innerHTML = "00:00";
    this.bg.style.backgroundColor = "#0f9d58";
    this.timerLabel.style.color = "white";
	}


function getTime(time) {

  var min = Math.floor(time/100/60);
  var sec = Math.floor(time/100);

  if (min < 10) {
    min = "0" + min;
  }
  if (sec >= 60) {
    sec = sec % 60;
  }
  if (sec < 10) {
    sec = "0" + sec;
  }

  return min + ":" + sec;

}

init();
