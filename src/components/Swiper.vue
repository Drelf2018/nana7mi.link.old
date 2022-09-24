<template>
    <div id="swiperBox" @mouseenter="stop" @mouseleave="start" :style="{'height': height}">
        <div class="hidden">
            <div id="swiper">
                <div class="imgDiv" v-for="obj in banner">
                    <a :href="obj.link">
                        <img class="swiper-width" :src="obj.url">
                        <img class="swiper-height" :src="obj.url">
                    </a>
                </div>
            </div>
        </div>
        <ion-icon name="chevron-back-circle" class="btn" style="left: 10px" @click="moveNow(-1)"></ion-icon>
        <ion-icon name="chevron-forward-circle" class="btn" style="right: 10px" @click="moveNow(1)"></ion-icon>
    </div>
</template>

<script>
export default {
    name: 'Swiper',
    props: {
        speed: String,
        height: String,
        banner: null
    },
    data() {
        return {
            timer: null,
            count: 0,
            swiper: null,
            lsatMove: new Date().getTime()
        }
    },
    updated() {
        this.total = this.banner.length;
        this.swiper.style.width = this.total + '00%';
        var maxAlpha = 0;
        this.banner.forEach(
            obj => {
                var currentImg = new Image();
                currentImg.src = obj.url;
                setTimeout(() => {
                    var alpha = currentImg.width / currentImg.height;
                    if(alpha > maxAlpha) maxAlpha = alpha;
                }, 100);
            }
        )
        setTimeout(() => {
            document.getElementById('swiperBox').style.width = maxAlpha * parseInt(this.height) + 'px';
        }, 300);
    },
    methods: {
        stop() {
            if (this.timer) {
                clearInterval(this.timer);
                this.timer = null;
            }

        },
        start() {
            var that = this;
            function autoScroll() {
                that.count += 1;
                that.swiper.style.transition = "all 0.5s";
                that.swiper.style.left = -100 * that.count + '%';
                if (that.count >= that.total - 1)
                    setTimeout(() => {
                        that.swiper.style.transition = "none";
                        that.swiper.style.left = '0%';
                        that.count = 0;
                    }, 505);
            }
            this.timer = setInterval(autoScroll, parseInt(this.speed));
        },
        moveNow(fro) {
            var tt = new Date().getTime();
            if (tt - this.lsatMove > 505) this.lsatMove = tt;
            else return;
            this.stop();
            if (this.swiper.style.left) {
                this.count = parseInt(this.swiper.style.left)/-100 + fro;
            } else {
                this.count = fro;
            }
            if (this.count >= this.total - 1) {
                this.count = 0;
                this.swiper.style.left = -100 * (this.total - 1) + '%';
                setTimeout(() => {
                    this.swiper.style.transition = "none";
                    this.swiper.style.left = '0%';
                    setTimeout(() => {
                        this.swiper.style.transition = "all 0.5s";
                    }, 30);
                }, 505);
            }
            else if (this.count < 0) {
                this.count = this.total - 2;
                this.swiper.style.transition = "none";
                this.swiper.style.left = -100 * (this.total - 1) + '%';
                setTimeout(() => {
                    this.swiper.style.transition = "all 0.5s";
                    this.swiper.style.left = -100 * this.count + '%';
                }, 30);
            }
            else this.swiper.style.left = -100 * this.count + '%';
        }
    },
    mounted() {
        this.swiper = document.getElementById('swiper');
        this.start();
    },
    beforeDestroy() {
        this.stop();
    }
}
</script>

<style>
#swiperBox {
    width: 0px;
    height: 250px;
    position: relative;
    border-radius: 10px;
    box-shadow: 0 7px 10px grey;
    z-index: 2;
}

.btn {
    color: #FFF;
    font-size: 40px;
    height: 20%;
    top: 40%;
    position: absolute;
    cursor: pointer;
    transition: all 0.3s;
    opacity: 0.5;
}

#swiperBox:hover .btn {
    opacity: 1;
}

.hidden {
    width: 100%;
    height: 100%;
    overflow: hidden;
    border-radius: 10px;
}

#swiper {
    left: 0%;
    position: relative;
    height: 100%;
    display: flex;
    transition: all 0.5s;
}

.imgDiv {
    width: 100%;
    height: 100%;
    position: relative;
    overflow:hidden;
}

img.swiper-width {
    width: 100%;
    height: 105%;
    position: absolute;
    filter: blur(5px);
    opacity: 0.5;
}

img.swiper-height {
    height: 100%;
    left: 0;
    right: 0;
    position: absolute;
    margin: auto;
}
</style>
