<template>
    <div>
    <button @click="like">좋아요</button>
    {{article?.like_users.length}}
    {{article.id}}
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'ArticleLike',
    props:{
        article:Object
    },
    // data(){
    //     return{
    //         article:this.article,
    //     }
    // },
    computed: {
        isLogin() {
            return this.$store.getters.isLogin
        }
        ,
        userInfo() {
            return this.$store.state.userInfo
            }
    },
    methods:{
        like(){
            axios({
                method: 'post',
                url: `${API_URL}/articles/${this.$route.params.id}/likes/`,
                headers:{
                    Authorization: `Token ${this.$store.state.token}`
        },

            })
            .then((res)=>{
                console.log(res)
                this.article = res.data
            })
            .catch(err => console.log(err))
        }
    }
    ,
    methods:{
        like(){
            axios({
                method: 'post',
                url: `${API_URL}/articles/${this.$route.params.id}/likes/`,
                headers:{
                    Authorization: `Token ${this.$store.state.token}`
        },

            })
            .then((res)=>{
                console.log(res)
                this.article = res.data
            })
            .catch(err => console.log(err))
        },
    //     check() {
    //         console.log(this.article.like_users.includes(this.userInfo.pk))
    //         if (this.article.like_users.includes(this.userInfo.pk)) {
    //             this.$store.dispatch('getArticle')
    //             return true
    //         }
    //         else {
    //             this.$store.dispatch('getArticle')
    //             return false
    //         }

    // }

}}
</script>

<style>

</style>