# 2018 선린 고등해커 'YoungWave' 팀 Write-ups
작성자 : 백창인

> **Index**
> 1. [Rev] BPPT - 200pt
> 2. [Rev] Ego - 100pt
> 3. [Web] Special Login - 150pt
> 4. [Misc] Beep and daum yo - 80pt
> 5. [Misc] What's mean? - 50pt

## [**Reversing**]

### BPPT - 200pt

우선 문제 파일을 다운로드 받으면 파워포인트 형식의 파일인 것을 확인할 수 있습니다. Mac OS X 환경에서 키노트만으로는 해결하기 어려운 문제이기 떄문에 Windows 데스크탑을 이용했습니다.

문제 파일을 실행해 Check 버튼 우클릭 -> 코드 보기를 클릭하면 Microsoft Visual Basic으로 작성된 버튼 클릭 시 실행 코드를 아래와 같이 확인할 수 있습니다.

```
Private Sub CommandButton1_Click()
    Dim flg As String
    flg = TextBox1.Text
    
    Dim bt(10, 100) As Boolean

    For i = 0 To 7
        For j = 0 To Len(flg) - 1
            bt(i, j) = ((Asc(Mid(flg, j + 1, 1))) And (1 * (2 ^ i))) = 0
        Next
    Next

    Dim fla(12, 100) As Boolean
    fla(0, 0) = False
    fla(0, 1) = False
    ...

    Dim flagage As Boolean
    flagage = True
    
    For i = 0 To 7
        For j = 0 To Len(flg) - 1
            flagage = flagage And (fla(i, j) = bt(i, j))
        Next
    Next
    
    If flagage And Len(flg) = 31 Then
        TextBox1.Text = "That is Flag"
    Else
        TextBox1.Text = "NOPE"
    End If
End Sub
```

위 코드를 간단히 분석해 보면, 입력받은 문자열을 바이트 단위로 쪼개어 각 비트의 자리수마다 0이면 True, 1이면 False임을 2차원 배열에 Boolean 형태로 저장하여 fla 배열과 비교해 모두 같으면 정답입니다.

이런 형태의 문제는 간단하게 스크립트를 짜 역연산 해주면 됩니다.

```python
fla = [[0]*100 for i in range(12)]
flag = []

for i in range(31):
    flag.append(0)

fla[0][0] = 0       #1의 자리 0이면 1
fla[0][1] = 0
fla[0][2] = 1
fla[0][3] = 1
fla[0][4] = 0
fla[0][5] = 1
fla[0][6] = 0
fla[0][7] = 1
fla[0][8] = 0
fla[0][9] = 1
fla[0][10] = 0
fla[0][11] = 1
fla[0][12] = 0
fla[0][13] = 0
fla[0][14] = 1
fla[0][15] = 1
fla[0][16] = 1
fla[0][17] = 1
fla[0][18] = 0
fla[0][19] = 0
fla[0][20] = 1
fla[0][21] = 0
fla[0][22] = 1
fla[0][23] = 0
fla[0][24] = 0
fla[0][25] = 1
fla[0][26] = 1
fla[0][27] = 0
fla[0][28] = 0
fla[0][29] = 0
fla[0][30] = 0
fla[1][0] = 0       #2의 자리 0이면 1
fla[1][1] = 1
fla[1][2] = 0
fla[1][3] = 0
fla[1][4] = 1
fla[1][5] = 0
fla[1][6] = 0
fla[1][7] = 1
fla[1][8] = 0
fla[1][9] = 0
fla[1][10] = 1
fla[1][11] = 0
fla[1][12] = 0
fla[1][13] = 0
fla[1][14] = 1
fla[1][15] = 1
fla[1][16] = 1
fla[1][17] = 0
fla[1][18] = 0
fla[1][19] = 0
fla[1][20] = 0
fla[1][21] = 1
fla[1][22] = 0
fla[1][23] = 0
fla[1][24] = 0
fla[1][25] = 0
fla[1][26] = 1
fla[1][27] = 1
fla[1][28] = 0
fla[1][29] = 1
fla[1][30] = 1
fla[2][0] = 1
fla[2][1] = 0
fla[2][2] = 0
fla[2][3] = 1
fla[2][4] = 1
fla[2][5] = 0
fla[2][6] = 1
fla[2][7] = 1
fla[2][8] = 0
fla[2][9] = 0
fla[2][10] = 1
fla[2][11] = 0
fla[2][12] = 0
fla[2][13] = 0
fla[2][14] = 1
fla[2][15] = 1
fla[2][16] = 0
fla[2][17] = 0
fla[2][18] = 0
fla[2][19] = 0
fla[2][20] = 0
fla[2][21] = 1
fla[2][22] = 0
fla[2][23] = 0
fla[2][24] = 0
fla[2][25] = 0
fla[2][26] = 0
fla[2][27] = 1
fla[2][28] = 0
fla[2][29] = 1
fla[2][30] = 0
fla[3][0] = 1
fla[3][1] = 1
fla[3][2] = 0
fla[3][3] = 1
fla[3][4] = 0
fla[3][5] = 0
fla[3][6] = 0
fla[3][7] = 1
fla[3][8] = 1
fla[3][9] = 0
fla[3][10] = 0
fla[3][11] = 0
fla[3][12] = 1
fla[3][13] = 0
fla[3][14] = 1
fla[3][15] = 1
fla[3][16] = 1
fla[3][17] = 1
fla[3][18] = 0
fla[3][19] = 1
fla[3][20] = 0
fla[3][21] = 0
fla[3][22] = 0
fla[3][23] = 1
fla[3][24] = 0
fla[3][25] = 1
fla[3][26] = 0
fla[3][27] = 1
fla[3][28] = 1
fla[3][29] = 1
fla[3][30] = 0
fla[4][0] = 0
fla[4][1] = 0
fla[4][2] = 1
fla[4][3] = 0
fla[4][4] = 1
fla[4][5] = 1
fla[4][6] = 0
fla[4][7] = 0
fla[4][8] = 0
fla[4][9] = 1
fla[4][10] = 1
fla[4][11] = 1
fla[4][12] = 1
fla[4][13] = 0
fla[4][14] = 0
fla[4][15] = 0
fla[4][16] = 0
fla[4][17] = 1
fla[4][18] = 1
fla[4][19] = 0
fla[4][20] = 1
fla[4][21] = 1
fla[4][22] = 1
fla[4][23] = 1
fla[4][24] = 0
fla[4][25] = 1
fla[4][26] = 1
fla[4][27] = 1
fla[4][28] = 1
fla[4][29] = 1
fla[4][30] = 0
fla[5][0] = 1
fla[5][1] = 0
fla[5][2] = 0
fla[5][3] = 0
fla[5][4] = 0
fla[5][5] = 0
fla[5][6] = 0
fla[5][7] = 0
fla[5][8] = 0
fla[5][9] = 0
fla[5][10] = 0
fla[5][11] = 0
fla[5][12] = 0
fla[5][13] = 1
fla[5][14] = 1
fla[5][15] = 1
fla[5][16] = 1
fla[5][17] = 0
fla[5][18] = 0
fla[5][19] = 0
fla[5][20] = 0
fla[5][21] = 0
fla[5][22] = 0
fla[5][23] = 0
fla[5][24] = 1
fla[5][25] = 0
fla[5][26] = 0
fla[5][27] = 0
fla[5][28] = 0
fla[5][29] = 0
fla[5][30] = 0
fla[6][0] = 0
fla[6][1] = 0
fla[6][2] = 0
fla[6][3] = 0
fla[6][4] = 0
fla[6][5] = 0
fla[6][6] = 0
fla[6][7] = 0
fla[6][8] = 0
fla[6][9] = 0
fla[6][10] = 0
fla[6][11] = 0
fla[6][12] = 0
fla[6][13] = 0
fla[6][14] = 0
fla[6][15] = 0
fla[6][16] = 0
fla[6][17] = 1
fla[6][18] = 0
fla[6][19] = 0
fla[6][20] = 0
fla[6][21] = 0
fla[6][22] = 0
fla[6][23] = 0
fla[6][24] = 0
fla[6][25] = 0
fla[6][26] = 0
fla[6][27] = 0
fla[6][28] = 0
fla[6][29] = 1
fla[6][30] = 0
fla[7][0] = 1
fla[7][1] = 1
fla[7][2] = 1
fla[7][3] = 1
fla[7][4] = 1
fla[7][5] = 1
fla[7][6] = 1
fla[7][7] = 1
fla[7][8] = 1
fla[7][9] = 1
fla[7][10] = 1
fla[7][11] = 1
fla[7][12] = 1
fla[7][13] = 1
fla[7][14] = 1
fla[7][15] = 1
fla[7][16] = 1
fla[7][17] = 1
fla[7][18] = 1
fla[7][19] = 1
fla[7][20] = 1
fla[7][21] = 1
fla[7][22] = 1
fla[7][23] = 1
fla[7][24] = 1
fla[7][25] = 1
fla[7][26] = 1
fla[7][27] = 1
fla[7][28] = 1
fla[7][29] = 1
fla[7][30] = 1

for i in range(31): #0~30
    flag[i] = 0
    for j in range(8): #0~7
        a = 1
        if(fla[j][i] == 1):
            a = 0
        flag[i] += a * (2**j)
    print(chr(flag[i]),end='')
print()
```

    Sunrin{pwning_PPT&owning_flag!}

### Ego - 100pt

우선 문제 파일을 다운로드 받으면 우리가 일반적으로 알고 있는 .py 확장자가 아닌 .pyc형태의 바이트코드로 컴파일된 파일 형식의 확장자를 볼 수 있습니다. 이 pyc 파일은 원본 py 파일 없이도 빠르게 실행할 수 있습니다.

하지만 이러한 pyc 파일도 원본 py 파일로 디컴파일 할 수 있는 방법이 있습니다. 아래와 같이 Uncompyle6를 이용해 봅시다.

> $ pip install uncompyle6
> 
> $ uncompyle6 ego.pyc

디컴파일을 완료하면 다음과 같은 .py 파일을 얻을 수 있습니다.

```python
import hashlib
i = input().strip()
k = hashlib.new('md5')
k.update(i.encode())
if i.split('_') == ['Sunrin{this', 'is', 'flag', '', 'lool', '', '}'] and k.digest() == 'Y\xa8\x07-P$\xdc\xcc\x02C\x1a#\xf5\xc4\xd1\x97':
    print('OK')
else:
    print('NOPE')
# okay decompiling Ego.pyc
```

코드를 간단히 해석해보면, 입력받은 문자열을 언더바 단위로 split한 것을 비교하고 있기 때문에 조건이 참이 되는 문자열은 Sunrin{this_is_flag__lool__}가 됩니다. 뒤의 digest() 함수는 md5로 인코딩 된 문자열을 비교하는 것 같습니다.

인증하면 정답인 것을 확인할 수 있습니다.

	Sunrin{this_is_flag__lool__}

## [**Web**]

### Special Login - 150pt

사실 웹해킹을 많이 접해보진 않았지만 그나마 몇 번 워게임으로 경험해본 화이트박스 문제였기 때문에 도전해 보았습니다.

```php
<?php 
error_reporting(0); 
require_once 'flag.php'; 

if(isset($_GET['source'])) { 
    show_source(__FILE__); 
} 

if(isset($_GET['login'])) { 
     
    if(is_numeric($_POST['username']) || is_numeric($_POST['password'])) { 
        echo '<h4>(つﾟ⊿ﾟ)つ Non-numeric characters are required.</h4>'; 
    } 
    else { 
        $username = md5($_POST['username']); 
        $password = sha1($_POST['password']); 

        if($username == $password) { 
            die('<h1>(^Д^)ﾌﾟ Congrats-! flag is '.$flag.'</h1>'); 
        } 
        else { 
            echo '<h4>(ヽ´ω`) Login failed</h4>'; 
        } 
    } 
} 
?> 
```

코드를 분석해 봅시다. 입력받은 id와 pw는 숫자로만 이루어지면 안 되며, md5, sha1로 각각 해싱한 것을 == 연산자로 비교해 참이 되면 Flag를 출력하게 되는 로직입니다.

우선 php에서 == 연산자는 0e로 시작하는 지수 표현식 numeric 간에 대한 비교 연산에서 심각한 취약점을 가지고 있습니다. 위 조건에 해당하는 피연산자면 무조건 참이 되는 문제점을 가지고 있죠.

우리는 이 취약점과 magic hash라는 것을 이용하여 문제를 해결했습니다. magic hash란 특정 문자열을 md5, sha1등의 해시 생성 알고리즘으로 해싱 했을 때 생기는 0e로 시작하는 numeric hash들을 말합니다.

대표적으로 md5에서는 "QNKCDZO"를 인코딩 하면 "0e830400451993494058024219903391", sha1에서 "aaO8zKZF"를 인코딩 하면 "0e89257456677279068558073954252716165668"라는 해시를 얻을 수 있습니다.

놀랍게도 이 둘은 다르지만 == 비교 연산을 하면 참이라는 결과 값을 반환합니다.

	ID : QNKCDZO
	PW : aaO8zKZF
	Sunrin{0ae0ae0a0ea0ea0ea0ea0ea0ea0e0ae0ae}

## [**Misc**] 

### Beep and daum yo - 80pt

이런. 문제 설명 그대로입니다. 그림판을 켜고 열심히 바코드를 복구한 뒤 online-barcode-reader.inliteresearch.com에서 바코드를 인식시켜 줍시다. 손목 스킬이 필요한 문제입니다.

	Sunrin{BeepBeep}

## What's mean? - 50pt

각종 CTF에 단골 Misc 문제로 등장하는 문제입니다. -는 1로, _는 0으로 치환해 바이트 단위로 쪼개어 아스키코드 값을 문자로 바꿔줍시다.

```python
# -*- coding: utf-8 -*-
str = ['01010011', '01110101', '01101110', '01110010', '01101001', '01101110', '01111011', '01000100', '00110000', '01011111', '01111001', '00110000', '01110101', '01011111', '01101011', '01101110', '00110000', '01110111', '01011111', '01100010', '00110001', '01101110', '00110100', '01110010', '01111001', '00111111', '01111101']

for i in str:
    print(chr(int(i,2)),end='')
print()
```

	Sunrin{D0_y0u_kn0w_b1n4ry?}