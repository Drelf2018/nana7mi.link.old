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
            count: 1,
            swiper: null
        }
    },
    updated() {
        this.total = this.banner.length;
        var maxAlpha = 0;
        Array.from(this.swiper.children).forEach(
            pp => {
                var img = pp.lastChild.lastChild
                var alpha = img.width / img.height;
                if(alpha > maxAlpha) maxAlpha = alpha;
            }
        )
        document.getElementById('swiperBox').style.width = maxAlpha * parseInt(this.height) + 'px';
        this.swiper.style.width = this.total + '00%';
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
                that.swiper.style.left = -100 * that.count + '%';
                that.count += 1;
                if (that.count >= that.total) that.count = 0;
            }
            this.timer = setInterval(autoScroll, parseInt(this.speed));
        },
        moveNow(fro) {
            this.stop();
            if (this.swiper.style.left) {
                this.count = parseInt(this.swiper.style.left)/-100 + fro;
            } else {
                this.count = fro;
            }
            if (this.count >= this.total) this.count = 0;
            if (this.count < 0) this.count = this.total - 1;
            this.swiper.style.left = -100 * this.count + '%';
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
    width: 447px;
    /* margin: 20px auto; */
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
    transition: all 1s;
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
