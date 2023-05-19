<template>
  <div>
    맞춤형 상품 추천

    <table border="1">
        <th>선택</th>
        <tr>
            <td>성별</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.female">여자
                <input type="checkbox" name="tendency" v-model="info.male">남자
            </td>
        </tr>
        <tr>
            <td>나이</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.age_one">20세 이하
                <input type="checkbox" name="tendency" v-model="info.age_two">20세 ~ 29세
                <input type="checkbox" name="tendency" v-model="info.age_three">30세 ~ 40세
                <input type="checkbox" name="tendency" v-model="info.age_four">40세 ~ 49세
                <input type="checkbox" name="tendency" v-model="info.age_five">50세 ~ 59세
                <input type="checkbox" name="tendency" v-model="info.age_six">60세 이상
            </td>
        </tr>
        <tr>
            <td>연봉</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.sal_one">2000만원 이하
                <input type="checkbox" name="tendency" v-model="info.sal_two">2000만원 ~ 4000만원
                <input type="checkbox" name="tendency" v-model="info.sal_three">4000만원 ~ 6000만원
                <input type="checkbox" name="tendency" v-model="info.sal_four">6000만원 ~ 8000만원
                <input type="checkbox" name="tendency" v-model="info.sal_five">8000만원 ~ 10000만원
                <input type="checkbox" name="tendency" v-model="info.sal_six">10000만원 이상
            </td>
        </tr>
        <tr>
            <td>자산</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.whl_one">2000만원 이하
                <input type="checkbox" name="tendency" v-model="info.whl_two">2000만원 ~ 6000만원
                <input type="checkbox" name="tendency" v-model="info.whl_three">6000만원 ~ 10000만원
                <input type="checkbox" name="tendency" v-model="info.whl_four">10000만원 ~ 20000만원
                <input type="checkbox" name="tendency" v-model="info.whl_five">20000만원 ~ 40000만원
                <input type="checkbox" name="tendency" v-model="info.whl_six">40000만원 이상
            </td>
        </tr>
        <tr>
            <td>저축성향</td>
            <td>
                <input type="checkbox" name="tendency" v-model="info.short">단기
                <input type="checkbox" name="tendency" v-model="info.middle">중기
                <input type="checkbox" name="tendency" v-model="info.long">장기
            </td>
        </tr>
    </table>
  </div>

</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'Recommend',
    data(){
        return {
            info : {
            female : false, male : false,
            age_one : false, age_two : false, age_three : false, age_four : false, age_five : false, age_six : false,
            sal_one : false, sal_two : false, sal_three : false, sal_four : false, sal_five : false, sal_six : false,
            whl_one : false, whl_two : false, whl_three : false, whl_four : false, whl_five : false, whl_six : false,
            short : false, middle : false, long : false
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
            console.log(response)
            })
            .catch((err) => {
            console.log(err)
            })
        }
    },
    watch : {
      info : {
        handler(val,oldval) {
            this.get_deposit_sorted()
        },
        deep:true,
      }
    },
}

</script>

<style>

</style>