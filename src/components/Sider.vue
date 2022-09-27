<template>
    <div class="hidden-sider" style="left: -100%">
        <div style="overflow: auto; height: 100%">
            <div class="content">
                <h2 style="margin-top: 0.7em; margin-bottom: 0.3em">本页面</h2>
                <div style="display: flex;justify-content: space-between; margin-bottom: 1.75em;">
                    <div class="link">
                        <ion-icon name="logo-github" id="github"></ion-icon>
                        <div style="display: inline;">
                            <a href="https://github.com/Drelf2018/nana7mi.link">
                                <strong>前端</strong><br />
                                <span style="color: grey;">VUE 3</span></a>
                        </div>
                    </div>
                    <div class="link">
                        <ion-icon name="logo-github" id="github"></ion-icon>
                        <div style="display: inline;">
                            <a href="https://github.com/Drelf2018/api.nana7mi.link">
                                <strong>后端</strong><br />
                                <span style="color: grey;">PY 3.10</span></a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content" v-for="(val, key) of repositories">
                <h2 style="margin-top: 0.7em; margin-bottom: 0.3em">{{ key }}</h2>
                <ul style="margin: 0; padding-left: 0;">
                    <li v-for="r in val">
                        <a :href="r.name ? ('https://github.com/' + r.name) : r.url">
                            <img :src="r.uid ? ('https://avatars.githubusercontent.com/u/' + r.uid + '?s=16') : r.src"
                                class="avatar">
                        </a>
                        <a class="repositories" :href="r.name ? ('https://github.com/' + r.name) : 'https://' + r.url">
                            {{ r.name ? r.name : r.url }}
                        </a>
                    </li>
                </ul>
            </div>

            <div class="content">
                <h2 style="margin-top: 0.7em; margin-bottom: 0.3em">关于</h2>
                随便说点什么吧。<br />
                <em>鼠标放在最上面的眼睛试试？</em>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Sider',
    data() {
        return {
            repositories: {
                'UI 抄袭自': [
                    { uid: 15519693, name: 'AceDroidX/SuperSpider' },
                    { uid: 10243794, name: 'brainbush/matsuri.icu' },
                    { uid: 22138497, name: 'vuetifyjs/vuetify' },
                    { src: 'https://penguin-stats.cn/favicon.ico', url: 'penguin-stats.cn' },
                    { src: 'https://prts.wiki/favicon.ico', url: 'prts.wiki' },
                ]
            }
        }
    }
}
</script>

<style>
.link {
    display: flex;
    width: 48%;
    transition: all 0.1s;
    border-radius: 0.5em;
    box-shadow: 0 2px 5px grey;
}

.link:hover {
    background-color: rgb(245, 245, 245);
    box-shadow: 0 1px 3px grey;
}

#github {
    margin: auto 0;
    padding: 0 0.2em;
    font-size: 1.8em;
    transition: all 0.1s;
}

.hidden-sider {
    top: 56px;
    width: 20%;
    height: calc(200vh - 56px);
    position: fixed;
    background-color: #FFF;
    border-right: 1px solid rgb(216, 222, 228);
    z-index: 2;
}

@media screen and (max-width: 900px) {
    .hidden-sider {
        width: 100%;
    }
}

.content {
    width: 80%;
    margin: 0 auto;
}

li {
    list-style: none;
    display: block;
    padding-bottom: 0.5em;
}

.avatar {
    width: 16px;
    height: 16px;
    float: left;
    overflow: hidden;
    line-height: 1;
    vertical-align: middle;
    flex-shrink: 0;
    box-shadow: 0 0 0 1px grey;
    border-radius: 50%;
    margin: 0 0.5em 0.5em 0;
}

.repositories {
    color: #24292f;
}

.repositories:hover {
    text-decoration: underline;
}
</style>
