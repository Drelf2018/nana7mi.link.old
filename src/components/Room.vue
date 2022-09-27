<template>
    <div class="show-block live">
        <a :href="room.cover">
            <img class="cover" :alt="room.cover" :src="room.cover" :style="room.cover ? '' : 'opacity: 0;'">
        </a>
        <div class="info">
            <a :href="'https://space.bilibili.com/' + room.uid" style="color: #000"><strong>{{ room.username }}</strong></a>
            <a v-show="!room.sp" class="tag living" :href="'https://live.bilibili.com/' + room.room">直播中</a>
            <a v-show="room.sp" class="tag prepare" :href="'https://live.bilibili.com/' + room.room">下播了</a>
            <div class="data">
                <div class="column" v-for="(value, key) in info">
                    <p class="time">{{ key }}</p>
                    <strong>{{ value }}</strong>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Room',
    props: {
        room: Object
    },
    mounted() {
        var self = document.getElementById(this.room.room + '_' + this.room.st);
        setTimeout(() => {
            self.style.opacity = 1;
            self.style.left = "0%";
        }, 1)
    },
    updated() {
        var self = document.getElementById(this.room.room + '_' + this.room.st);
        self.style.opacity = 1;
        self.style.left = "0%";
    },
    methods: {
        format(tt) {
            if (tt) return new Date(tt * 1000).Format("yyyy-MM-dd hh:mm:ss");
            else return '直播中';
        }
    },
    computed: {
        info() {
            return {
                '标题': this.room.title,
                '开始': this.format(this.room.st),
                '结束': this.format(this.room.sp),
                '营收': this.room.sp ? (this.room.guard_buy + this.room.send_gift + this.room.super_chat_message).toFixed(2) : "暂无"
            }
        }
    }
}
</script>

<style>
.tag {
    color: #FFF;
    font-weight: 700;
    margin-left: 0.5em;
    padding: 0.3em 0.4em;
    border-radius: 0.25em;
}

.living {
    background-color: rgb(13, 110, 253);
}

.prepare {
    background-color: rgb(57, 172, 72);
}

.cover {
    width: 196px;
    height: 110px;
    float: left;
    margin-right: 1em;
    border-radius: 5px;
    box-shadow: 0 3px 6px grey;
}

.show-block {
    position: relative;
    margin-bottom: 1em;
    overflow: hidden;
    border-radius: 5px;
    background-color: #FFF;
    box-shadow: 0 3px 1px -2px rgb(0 0 0 / 12%), 0 2px 2px 0 rgb(0 0 0 / 14%), 0 1px 5px 0 rgb(0 0 0 / 20%)
}

.live {
    padding: 1em; 
    transition: background-color 0.2s ease 0s, opacity 0.5s ease 0s, left 0.5s ease 0s;
}

.live:hover {
    background-color: hsl(225, 100%, 97%);
}

.time {
    color: grey;
}

/* 创建四个相等的列 */
.column {
    float: left;
    width: 25%;
}

.data {
    display: flex;
}

.info {
    margin-top: 0.5em;
}

/* 响应式布局 - 小于 900 px 时改为上下布局 */
@media screen and (max-width: 900px) {
    .time {
        display: inline-block;
        margin: 0.5em 0.5em 0 0;
    }

    .column {
        width: 100%;
    }

    .data {
        flex-direction: column;
    }

    .cover {
        float: none;
    }
}
</style>