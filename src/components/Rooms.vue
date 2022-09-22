<template>
    <div class="live">
        <a :href="'https://space.bilibili.com/' + room.uid">
            <img class="cover" alt="" :src="room.cover">
        </a>
        <div style="margin-top: 26px">
            <div>
                <h3 class="name">{{ room.username }}</h3>
                <a v-show="!room.sp" class="living" :href="'https://live.bilibili.com/' + room.room">直播中</a>
            </div>
            <div style="vertical-align: baseline; display: flex">
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
    name: 'Rooms',
    props: {
        room: Object
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
                '营收': (this.room.guard_buy + this.room.send_gift + this.room.super_chat_message).toFixed(2)
            }
        }
    }
}
</script>

<style>
h3.name {
    margin: 0;
    display: inline-block;
    padding-right: 5px;
}

a.living {
    color: #FFF;
    font-weight: 700;
    padding: 0.4em 0.5em;
    border-radius: 0.25em;
    background-color: rgb(13, 110, 253);
}

img.cover {
    width: 196px;
    height: 110px;
    float: left;
    margin: 20px;
    border-radius: 10px;
    box-shadow: 0 7px 10px grey;
    transition: all 0.3s;
}

img.cover:hover {
    opacity: 0.7;
}

div.live {
    width: 85%;
    margin: 0px 15%;
    overflow: auto;
    /* border: 3px solid green; */
    overflow: hidden;
}

p.time {
    color: grey;
}

/* 创建四个相等的列 */
.column {
    float: left;
    width: 25%;
}

/* 响应式布局 - 小于 600 px 时改为上下布局 */
@media screen and (max-width: 600px) {
    .column {
        margin-left: 20px;
        width: 100%;
    }

    h3.name {
        margin-left: 20px;
    }
}
</style>