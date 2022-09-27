<template>
    <div class="danmaku" id="danmaku" style="opacity: 0;left: 100%;">
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
        danmaku: Object
    },
    data() {
        return {
            pos: 100
        }
    },
    computed: {
        splitDanmaku() {
            if (this.danmaku) return this.danmaku.slice(0, this.pos);
        }
    },
    updated() {
        var self = document.getElementById("danmaku");
        if (this.danmaku) {
            self.style.opacity = 1;
            self.style.left = "0%";
        } else {
            this.pos = 100;
            self.style.opacity = 0;
            self.style.left = "100%";
        }
    },
    mounted() {
        window.addEventListener('scroll', this.lazyLoading); // 滚动到底部，再加载的处理事件
    },
    methods: {
        lazyLoading () { // 滚动到底部，再加载的处理事件
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
    color: rgb(13,110,253);
}

.username:hover {
    text-decoration: underline;
}

.danmaku {
    position: relative;
    padding: 0 1em;
    margin-bottom: 1em;
    overflow: hidden;
    border-radius: 5px;
    transition: all 0.5s;
    background-color: #FFF;
    box-shadow: 0 3px 1px -2px rgb(0 0 0 / 12%), 0 2px 2px 0 rgb(0 0 0 / 14%), 0 1px 5px 0 rgb(0 0 0 / 20%)
}
</style>