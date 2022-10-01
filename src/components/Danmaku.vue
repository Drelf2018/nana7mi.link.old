<template>
    <div class="show-block danmaku" style="opacity: 0;left: 100%;">
        <div v-if="!index" style="float: right;width: 30%;display: flex;flex-direction: column;align-items: flex-end;">
            <input v-if="danmaku" v-model="button[6].timeStr" type="text" style="margin: 1em 0;" :placeholder="'时间筛选，默认不小于 ' + this.button[6].baseStr">
            <span v-if="danmaku"> 目前弹幕量：{{ this.splitDanmaku.length }} </span>
        </div>
        <p v-for="dm in splitDanmaku">
            {{ new Date(dm.time * 1000).Format(dm.room ? "yyyy-MM-dd hh:mm:ss" : "hh:mm:ss") }}
            <a class="username" :href="'https://space.bilibili.com/' + dm.uid" style="margin-left: 0.5em;">{{ dm.username }}</a>
            <span style="margin-left: 1em;" v-html="dm.msg"></span>
            <a style="margin-left: 1em;" :href="'https://live.bilibili.com/' + dm.room">
                <span style="color: grey"><em>{{ dm.room }}</em></span>
            </a>
        </p>
    </div>
</template>

<script>
export default {
    name: 'Danmaku',
    props: {
        danmaku: Object,
        button: [Object],
        index: 0
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
                if (this.button[0].status || this.button[1].status || this.button[2].status 
                 || this.button[3].maxPrice || this.button[4].content || this.button[6].timeStr
                 || this.index) {
                    var all = !this.button[0].status && !this.button[1].status && !this.button[2].status
                    var maxPrice = this.button[3].maxPrice ? this.button[3].maxPrice : 0
                    var check = this.analyse(this.button[4].content)
                    if (this.button[6].timeStr)
                        var tt = new Date(this.button[6].dateStr + ' ' + this.button[6].timeStr).getTime() / 1000
                    else var tt = 0
                    return this.danmaku.filter(
                        dm => {
                            if (this.index) return true
                            return dm.price >= maxPrice
                                && dm.time >= tt
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
        var self = document.getElementById("danmaku" + (this.index ? this.index : ''));
        if (this.danmaku) {
            self.style.opacity = 1;       
            self.style.left = "0%";
            setTimeout(() => this.button[5].mountedWait=1, 1000);
        } else {
            this.pos = 100;
            for (var i=0; i<this.button.length;i++) this.button[i].status = 0;
            self.style.opacity = 0;
            self.style.left = "100%";
        }
    },
    mounted() {
        if (!this.index) window.addEventListener('scroll', this.lazyLoading); // 滚动到底部，再加载的处理事件
        else {
            var self = document.getElementById("danmaku" + (this.index ? this.index : ''));
            setTimeout(() => {
                self.style.opacity = 1;
                self.style.left = "0%";
            }, 1)
        }
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

.danmaku {
    padding: 0 1em;
    transition: all 0.5s;
    overflow: hidden;
}
</style>