class AudioPalyer {


    constructor(track_path, track_image, track_name, track_artist, track_image_class,track_real_image,
        track_name_class, track_artist_class, track_body_class, playpause_btn, seek_slider, volume_slider,
        curr_time, total_duration) {

        this.track_image = track_image;
        this.track_name = track_name;
        this.track_artist = track_artist;
        this.track_image_class = track_image_class;
        this.track_real_image = track_real_image;
        this.track_name_class = track_name_class;
        this.track_artist_class = track_artist_class;
        this.track_body_class = track_body_class;
        // this.now_playing = now_playing;
        this.playpause_btn = playpause_btn;
        // this.next_btn = next_btn;
        // this.prev_btn = prev_btn;
        this.seek_slider = seek_slider;
        this.isSliding = false;

        this.volume_slider = volume_slider;
        this.curr_time = curr_time;
        this.total_duration = total_duration;

        // Audio element
        this.curr_track = document.createElement('audio');
        this.curr_track.autoplay = false;
        this.curr_track.preload = "metadate";

        this.isPlaying = false
        this.track_path = track_path;
        this.updateTimer;
        this.initFunction();
        this.loadTrack();
    }

    initFunction() {
        let classLevelThis = this;
        this.playpause_btn.onclick = function () {
            classLevelThis.playpauseTrack();
        }
        this.seek_slider.onchange = function () {
            classLevelThis.seekTo();
        }
        this.volume_slider.onchange = function () {
            classLevelThis.setVolume();
        }

        this.seek_slider.addEventListener('input', function () {
            classLevelThis.isSliding = true;
        });

        this.seek_slider.addEventListener('mouseup', function () {
            classLevelThis.isSliding = false;
        });

    }
    resetValues() {
        this.curr_track.currentTime = 0;
        this.seekUpdate();
        this.pauseTrack();
    }

    playTrack() {
        // Play the loaded track
        this.curr_track.play();
        this.isPlaying = true;
        // Replace icon with the pause icon
        this.playpause_btn.innerHTML = '<i class="fa fa-pause-circle fa-2x"></i>';

        // Set an interval of 1000 milliseconds
        // for updating the seek slider
        let classThis = this;
        // this.curr_track.onloadeddata = function(){
        classThis.updateTimer = setInterval(classThis.seekUpdate.bind(classThis), 100);
        // }
    }

    pauseTrack() {
        // Pause the loaded track
        this.curr_track.pause();
        this.isPlaying = false;
        // Replace icon with the play icon
        this.playpause_btn.innerHTML = '<i class="fa fa-play-circle fa-2x"></i>';
        clearInterval(this.updateTimer);
    }

    playpauseTrack() {
        // Switch between playing and pausing
        // depending on the current state
        if (!this.isPlaying) this.playTrack();
        else this.pauseTrack();
    }

    seekTo() {
        // Calculate the seek position by the
        // percentage of the seek slider 
        // and get the relative duration to the track
        let seekto = this.curr_track.duration * (this.seek_slider.value / 100);

        // Set the current track position to the calculated seek position
        this.curr_track.currentTime = seekto;
    }


    setVolume() {
        // Set the volume according to the
        // percentage of the volume slider set
        this.curr_track.volume = this.volume_slider.value / 100;
    }

    seekUpdate() {
        let seekPosition = 0;
        // Check if the current track duration is a legible number
        if (!isNaN(this.curr_track.duration)) {
            if (!this.isSliding) {
                seekPosition = this.curr_track.currentTime * (100 / this.curr_track.duration);
                this.seek_slider.value = seekPosition;
            }

            // Calculate the time left and the total duration
            let currentMinutes = Math.floor(this.curr_track.currentTime / 60);
            let currentSeconds = Math.floor(this.curr_track.currentTime - currentMinutes * 60);
            let durationMinutes = Math.floor(this.curr_track.duration / 60);
            let durationSeconds = Math.floor(this.curr_track.duration - durationMinutes * 60);

            // Add a zero to the single digit time values
            if (currentSeconds < 10) { currentSeconds = "0" + currentSeconds; }
            if (durationSeconds < 10) { durationSeconds = "0" + durationSeconds; }
            if (currentMinutes < 10) { currentMinutes = "0" + currentMinutes; }
            if (durationMinutes < 10) { durationMinutes = "0" + durationMinutes; }

            // Display the updated duration
            this.curr_time.textContent = currentMinutes + ":" + currentSeconds;
            this.total_duration.textContent = durationMinutes + ":" + durationSeconds;
        }
    }

    loadTrack() {

        // Clear the previous seek timer
        clearInterval(this.updateTimer);
        this.resetValues();

        // Load a new track
        this.curr_track.src = this.track_path;
        this.curr_track.load();

        // Update details of the track
        this.track_image_class.style.backgroundImage =
            "url(" + this.track_image + ")";
        this.track_body_class.style.backgroundImage =
            "linear-gradient(to right, rgb(118, 120, 121),#5b5b5b,var(--color1), var(--color2))";

        // initialize colorThief
        let colorThief = new ColorThief();
        // get color palette
        let color = colorThief.getColor(this.track_real_image);
        // set the background color
        this.track_body_class.style.backgroundImage =
            `linear-gradient(to right, rgb(${color}), var(--color2))`;
        if(this.track_name_class)
            this.track_name_class.textContent = this.track_name;
        if(this.track_artist_class)
            this.track_artist_class.textContent = this.track_artist;

        // Move to the next track if the current finishes playing
        // using the 'ended' event
        let classThis = this;
        this.curr_track.onloadeddata = function () {
            classThis.seekUpdate();
        }
        this.curr_track.addEventListener("ended", this.resetValues.bind(this));

        // Apply a random background color
        // random_bg_color();
    }
}