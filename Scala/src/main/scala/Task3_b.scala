import scala.io.StdIn.readInt

object Task3_b {
  def main(args: Array[String]) : Unit = {
    println("Введите годовой доход")
    val money = scala.io.StdIn.readInt()
    println("Введите размер премии в процентах")
    val pr: Double = scala.io.StdIn.readInt()
    println("Компенсация питания")
    val food = scala.io.StdIn.readInt()
    val sal_mon = money / 12
    val prem = (money * (pr/100)) / 12
    println(sal_mon + prem + food)
  }
}
