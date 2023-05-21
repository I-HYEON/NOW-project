<template>
  <div>
    맞춤형 상품 추천

    <table border="1">
        <th>선택</th>
        <tr>
            <td>성별</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.gen_two">여자
                <input type="checkbox" name="tendency" v-model="info.gen_one">남자
            </td>
        </tr>
        <tr>
            <td>나이</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.age_one">20세 이하
                <input type="checkbox" name="tendency" v-model="info.age_two">20세 ~ 29세
                <input type="checkbox" name="tendency" v-model="info.age_thr">30세 ~ 40세
                <input type="checkbox" name="tendency" v-model="info.age_fou">40세 ~ 49세
                <input type="checkbox" name="tendency" v-model="info.age_fiv">50세 ~ 59세
                <input type="checkbox" name="tendency" v-model="info.age_six">60세 이상
            </td>
        </tr>
        <tr>
            <td>연봉</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.sal_one">2000만원 이하
                <input type="checkbox" name="tendency" v-model="info.sal_two">2000만원 ~ 4000만원
                <input type="checkbox" name="tendency" v-model="info.sal_thr">4000만원 ~ 6000만원
                <input type="checkbox" name="tendency" v-model="info.sal_fou">6000만원 ~ 8000만원
                <input type="checkbox" name="tendency" v-model="info.sal_fiv">8000만원 ~ 10000만원
                <input type="checkbox" name="tendency" v-model="info.sal_six">10000만원 이상
            </td>
        </tr>
        <tr>
            <td>자산</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.whl_one">2000만원 이하
                <input type="checkbox" name="tendency" v-model="info.whl_two">2000만원 ~ 6000만원
                <input type="checkbox" name="tendency" v-model="info.whl_thr">6000만원 ~ 10000만원
                <input type="checkbox" name="tendency" v-model="info.whl_fou">10000만원 ~ 20000만원
                <input type="checkbox" name="tendency" v-model="info.whl_fiv">20000만원 ~ 40000만원
                <input type="checkbox" name="tendency" v-model="info.whl_six">40000만원 이상
            </td>
        </tr>
        <tr>
            <td>저축성향</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.ten_one">단기
                <input type="checkbox" name="tendency" v-model="info.ten_two">중기
                <input type="checkbox" name="tendency" v-model="info.ten_thr">장기
            </td>
        </tr>
    </table>
    <div class="container">
        <div v-if=show class="row">
            <DepositCard
            v-for="deposit in this.sorted_depositData"
            :deposit="deposit"
            :key="deposit.id"
            />
        </div>
        <div v-else>
            <img src="@/photo/loading.gif" alt="로딩중...">
        </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import DepositCard from '@/components/DepositCard.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'Recommend',
    components: {
        DepositCard
    },
    data(){
        return {
            show : false,
            sorted_depositData : [],
            info : {
            gen_one : false, gen_two : false,
            age_one : false, age_two : false, age_thr : false, age_fou : false, age_five : false, age_six : false,
            sal_one : false, sal_two : false, sal_thr : false, sal_fou : false, sal_five : false, sal_six : false,
            whl_one : false, whl_two : false, whl_thr : false, whl_fou : false, whl_five : false, whl_six : false,
            ten_one : false, ten_two : false, ten_thr : false
            },
        }
    },
    methods : {
        get_deposit_sorted() {
            const info = this.info
            axios({
                method: 'POST',
                url: `${API_URL}/deposits/recomend_deposit/`,
                data: info,
            })
            .then((response) => {
                this.sorted_depositData = response.data
                this.show = true
            })
            .catch((err) => {
            console.log(err)
            })
        }
    },
    watch : {
      info : {
        handler(val,oldval) {
            this.show = false
            this.get_deposit_sorted()
        },
        deep:true,
      }
    },
    created() {
        this.get_deposit_sorted()
    }
}

</script>

<style>

</style>