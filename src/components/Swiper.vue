<template>
    <div id="swiperBox" @mouseenter="stop" @mouseleave="start" :style="{'height': height}">
        <div class="hidden">
            <div id="swiper">
                <div class="imgDiv" v-for="(item,index) of imgList" :key="index">
                    <img class="swiper-width" :src="item">
                    <img class="swiper-height" :src="item">
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
        height: String
    },
    computed: {
        imgList() {
            if (this.banner) return this.banner.filter(b => b.location == "index_preview")
            else return [
                'https://prts.wiki/images/thumb/9/91/%E6%B4%BB%E5%8A%A8%E9%A2%84%E5%91%8A_%E9%95%BF%E5%A4%9C%E4%B8%B4%E5%85%892022_01.jpg/1170px-%E6%B4%BB%E5%8A%A8%E9%A2%84%E5%91%8A_%E9%95%BF%E5%A4%9C%E4%B8%B4%E5%85%892022_01.jpg',
                'https://prts.wiki/images/a/aa/%E6%B4%BB%E5%8A%A8%E9%A2%84%E5%91%8A_%E5%A5%BD%E4%B9%85%E4%B8%8D%E8%A7%81_01.jpg',
            ]
        }
    },
    data() {
        return {
            timer: null,
            count: 1,
            swiper: null
        }
    },
    methods: {
        clickLeft() {
            this.theDirection = 'left';
        },
        clickRight() {
            this.theDirection = 'right';
        },
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
        var that = this;
        axios
            .get('https://api.live.bilibili.com/xlive/web-interface/v1/index/getList?platform=web')
            .then((response) => that.banner = response.data.banner)
            .catch((error) => console.log(error));

        this.total = this.imgList.length;
        this.swiper = document.getElementById('swiper');
        var maxAlpha = 0;
        Array.from(this.swiper.children).forEach(
            (pp) => {
                var alpha = pp.lastChild.width / pp.lastChild.height;
                if(alpha > maxAlpha) maxAlpha = alpha;
            }
        )
        document.getElementById('swiperBox').style.width = maxAlpha * parseInt(this.height) + 'px';
        this.swiper.style.width = this.imgList.length + '00%';
        this.start();
    },
    beforeDestroy() {
        self.stop()
    }
}
</script>

<style>
#swiperBox {
    margin: 20px auto;
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

.btn:hover {
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
