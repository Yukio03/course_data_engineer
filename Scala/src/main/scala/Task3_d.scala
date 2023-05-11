object Task3_d {
  def main(args: Array[String]): Unit = {
    println("Введите годовой доход")
    val money = scala.io.StdIn.readInt()
    println("Введите размер премии в процентах")
    val pr: Double = scala.io.StdIn.readInt()
    println("Компенсация питания")
    val food = scala.io.StdIn.readInt()
    val sal_mon = money / 12
    val prem = (money * (pr / 100)) / 12
    /* премия в месяц */
    val salary = sal_mon + prem + food
    /* оклад сотрудника в месяц */
    val sal_dep = List(100, 150, 200, 80, 120, 75)
    val res = sal_dep :+ salary.toInt
    println("Максимальный оклад: ")
    println(res.max)
    println("Минимальный оклад: ")
    println(res.min)

  }
}