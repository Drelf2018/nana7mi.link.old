<template>
    <div class="show-block" id="danmaku" style="opacity: 0;left: 100%;">
        <p v-for="dm in splitDanmaku">
            {{ new Date(dm.time * 1000).Format("hh:mm:ss") }}&nbsp;&nbsp;
            <a class="username" :href="'https://space.bilibili.com/' + dm.uid">{{ dm.username }}</a>
            &nbsp;&nbsp;<span v-html="dm.msg"></span>
        </p>
    </div>
</template>

<script>
export default {
    name: 'Danmaku',
    props: {
        danmaku: Object,
        button: [Object]
    },
    data() {
        return {
            pos: 100
        }
    },
    computed: {
        splitDanmaku() {
            if (this.danmaku)
                if (this.button[0].status || this.button[1].status || this.button[2].status || this.button[3].status) {
                    var maxPrice = this.button[3].status ? 29.9 : this.button[2].status ? 19.9 : this.button[1].status ? 9.9 : 0
                    return this.danmaku.filter(
                        dm => {
                            return (!this.button[0].status || dm.type != "DANMU_MSG")
                                && (!maxPrice || dm.price > maxPrice)
                        }
                    )
                } else {
                    return this.danmaku.slice(0, this.pos)
                }
        }
    },
    updated() {
        var self = document.getElementById("danmaku");
        if (this.danmaku) {
            self.style.opacity = 1;       
            self.style.left = "0%";
        } else {
            this.pos = 100;
            for (var i=0; i<this.button.length;i++) this.button[i].status = 0;
            self.style.opacity = 0;
            self.style.left = "100%";
        }
    },
    mounted() {
        window.addEventListener('scroll', this.lazyLoading); // 滚动到底部，再加载的处理事件
    },
    methods: {
        lazyLoading() { // 滚动到底部，再加载的处理事件
            const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            const clientHeight = document.documentElement.clientHeight;
            const scrollHeight = document.documentElement.scrollHeight;
            if (scrollTop + clientHeight >= scrollHeight - 100) this.pos += 100;
        },
    }
}
</script>

<style>
.username {
    color: rgb(13, 110, 253);
}

.username:hover {
    text-decoration: underline;
}

#danmaku {
    padding: 0 1em;
    transition: all 0.5s;
    overflow: hidden;
}
</style>