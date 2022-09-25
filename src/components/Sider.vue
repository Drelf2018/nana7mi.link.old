<template>
    <div class="hidden-sider" style="left: -100%">
        <div style="overflow: auto; height: 100%">
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
                <input type="number" @change.lazy="(event) => callback(event.target.value, true)">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Sider',
    props: {
        callback: null
    },
    data() {
        return {
            repositories: {
                '相关仓库': [
                    { uid: 41439182, name: 'Drelf2018/nana7mi.link' },
                    { uid: 41439182, name: 'Drelf2018/api.nana7mi.link' }
                ],
                'UI抄袭来源': [
                    { uid: 15519693, name: 'AceDroidX/SuperSpider' },
                    { uid: 10243794, name: 'brainbush/matsuri.icu' },
                    { uid: 22138497, name: 'vuetifyjs/vuetify' },
                    { src: 'https://prts.wiki/favicon.ico', url: 'prts.wiki' }
                ]
            }
        }
    }
}
</script>

<style>
.hidden-sider {
    top: 56px;
    width: 20%;
    height: calc(100vh - 56px);
    position: fixed;
    background-color: #FFF;
    border-right: 1px solid rgb(216, 222, 228);
    z-index: 4;
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
