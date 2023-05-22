<template>
<div>
<h1> 프로필 페이지 입니다.</h1>
<p> 이름 : {{userInfo.username}}</p>
<p> 나이 : {{userInfo.age}}</p>
<p> 가입한 상품 : {{userInfo.deposit}}</p>
<p v-if="userInfo.gender === 1">성별 : 남자</p>
<p v-else>성별 : 여자</p>
<p> 연봉 : {{userInfo.salary}}만원</p>
<p v-if="userInfo.tendency === 1">투자성향 : 단기형</p>
<p v-else-if="userInfo.tendency === 2">투자성향 : 중기형</p>
<p v-else-if="userInfo.tendency === 3">투자성향 : 만기형</p>
<p> 재산 : {{userInfo.wealth}}만원</p>
<p> 유저pk : {{userInfo.pk}}</p>
<router-link to="profileupdate">회원정보 수정</router-link>

</div>
</template>

<script>
export default {
    name : 'ProfileView',
    computed: {
    isLogin() {
        return this.$store.getters.isLogin
    },
    userInfo() {
        console.log(this.$store.state.userInfo)
        return this.$store.state.userInfo
        
    }
},
}
</script>

<style>

</style>