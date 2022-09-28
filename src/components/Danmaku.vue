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
            pos: 100,
            Type: {
                "SEND_GIFT": 0,
                "GUARD_BUY": 1,
                "SUPER_CHAT_MESSAGE": 2,
                "DANMU_MSG": 3
            }
        }
    },
    computed: {
        splitDanmaku() {
            if (this.danmaku)
                if (this.button[0].status || this.button[1].status || this.button[2].status || this.button[3].maxPrice || this.button[4].content) {
                    var all = !this.button[0].status && !this.button[1].status && !this.button[2].status
                    var maxPrice = this.button[3].maxPrice ? this.button[3].maxPrice : 0
                    var check = this.analyse(this.button[4].content)
                    return this.danmaku.filter(
                        dm => {
                            return (dm.price >= maxPrice)
                                && (all || this.button[this.Type[dm.type]].status)
                                && check(dm.username + dm.msg)
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
        analyse(content) {
            if (!content) return (msg) => true
            content = content.split(" ")
            content.forEach((val, idx, arr) => arr[idx]=val.split("+"))
            return function(msg) {
                var i = null, j = null;
                for (i=0;i<content.length;i++) {
                    var flag = false, wlist=content[i];
                    for (j=0;j<wlist.length;j++) flag ||= msg.includes(wlist[j]);
                    if (!flag) return false;
                }
                return true;
            }
        }
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