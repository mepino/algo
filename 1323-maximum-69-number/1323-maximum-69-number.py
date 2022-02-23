class Solution:
    def maximum69Number (self, num: int) -> int:
        max_num = num
        str_num = str(num)
        point_location = 0
        while point_location < len(str(num)):
          list_str_num = list(str_num)

          # 해당자리 바꿀거 없으면 다음위치로 이동
          if list_str_num[point_location] == '9':
            point_location += 1
            continue
          else:
            list_str_num[point_location] = '9'
            point_location += 1
            max_cand = int(''.join(list_str_num))

            if max_cand > max_num:
              max_num = max_cand
        return max_num