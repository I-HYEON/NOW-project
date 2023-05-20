<template>
    <div>
        좋아요 페이지
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

}
</script>

<style>

</style>