### 函数
- js函数的参数并不会验证传递进来多少个参数, 也不会在乎传进来的参数是什么数据类型, 在函数体内可以用arguments对象来访问这个参数数组.
- arguments对象中的值会与命名参数的值同步修改, 即修改arguments值时会同步修改参数的值, 反之亦然.
- js中函数没有重载


### 变量和作用域
- 基本类型的复制是完全独立的复制值复制, 引用类型的复制实际上是复制的一份指针.
- js中所有函数的参数都是按值传递, 基本类型传递如同基本类型变量复制一样, 引用类型传递如同引用变量复制一样.
- try-catch语句的catch快和with语句会延长作用域链
- js中没有块级作用域, for/if花括号中定义的变量在花括号外也可访问.

### 引用变量
- Js中面向对象未实现面向对象的类和接口等基本结构，一般称为引用类型或对象定义。
- 访问对象的属性除了通用的`.`，还可使用`[]`，从而通过变量来访问对象属性。
- Js中每个函数都是Function类型的实例，因而与其他引用类型一样具有属性和方法。
- 函数内部有两个特殊对象arguments和this
  - arguments.callee 指向拥有这个arguments对象的函数。可用于消除与函数名的紧耦合
  - arguments.caller 保存着调用当前函数的函数的引用
  - this 对象引用的是函数据以执行的环境对象
```
function factorial(num) {
    if (num <= 1) {
        return 1;
    } else {
        return num * arguments.callee(num - 1); //factorial(num -1)
    }
}
```

```
function outer() {
    inner();
}
function inner() {
    alert(inner.caller);
}

outer(); //在警告窗中显示outer()的源代码
```

```
window.color = "red";
var o = {color: "blue"};

function sayColor() {
    alert(this.color);
}

sayColor()； //red

o.sayColor = sayColor;
o.sayColor(); //blue
```

- 函数中包含两个属性length和prototype
  - length 表示函数希望接收的命名参数个数
  - prototype 保存函数所有实例方法的真正所在，例如toString()和valueOf()等
- 每个函数包含的方法：apply()、call()和bind()
- 为了便于操作基本类型值，Js提供了基本类型的自动包装功能，每单读取一个基本类型值的时候，后台就会创建一个对应的基本包装类型的对象，并在调用后自动销毁。
  - 由于基本包装类型和基本类型的含义并不一样，会导致typeof等操作产生不同的结果，不推荐显示实例化基本数据类型