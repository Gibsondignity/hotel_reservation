import Link from "next/link";
import { BiMessageDetail } from "react-icons/bi";
import { BsFillSendFill, BsTelephoneOutbound } from "react-icons/bs";

const Footer = () => {
  return (
    <footer className="mt-16">
        <div className="container mx-auto px-4">
            <Link href="/" className="font-black text-tertiary-black">
                Eliana Homes
            </Link>
        

        <h4 className="font-bold text-[40px] py-6">Contact</h4>

        <div className="flex flex-wrap gap-16 items-center justify-between">
            <div className="flex-1">
                <p>123 Road</p>
                <div className="flex item-center py-4">
                    <BsFillSendFill />
                    <p className="ml-2">Code</p>
                </div>
                <div className="flex item-center py-4">
                    <BsTelephoneOutbound />
                    <p className="ml-2">Code</p>
                </div>
                <div className="flex item-center py-4">
                    <BiMessageDetail />
                    <p className="ml-2">Code</p>
                </div>
            </div>

            <div className="flex-1 md:text-right">
                <p className="pb-4">Our Story</p>
                <p className="pb-4">Get In Touch</p>
                <p className="pb-4">Our Privacy</p>
                <p className="pb-4">Terms of Service</p>
                <p>Customer Support</p>
            </div>

            <div className="flex-1 md:text-right">
                <div className="pb-4">Dinning Experience</div>
                <div className="pb-4">Welness</div>
                <div className="pb-4">Fitness</div>
                <div className="pb-4">Sports</div>
                <div>Events</div>
            </div>
        </div>
    </div>

        <div className="bg-tertiary-light h-10 md:h-[70px] mt-16 w-full bottom-0 left-0" />
    </footer>
  )
}

export default Footer