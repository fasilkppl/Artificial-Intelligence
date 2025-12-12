import { useState, useEffect } from "react";
import RadioSwitch from "./RadioSwitch";
import { Home, Bath, MapPin, Calculator, IndianRupee } from "lucide-react";
import { toast } from "@/hooks/use-toast";

const PricePredictor = () => {
  const [sqft, setSqft] = useState<string>("1000");
  const [bhk, setBhk] = useState<number>(2);
  const [bathrooms, setBathrooms] = useState<number>(2);
  const [location, setLocation] = useState<string>("");
  const [locations, setLocations] = useState<string[]>([]);
  const [estimatedPrice, setEstimatedPrice] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // Fetch locations from API
    const fetchLocations = async () => {
      try {
        const response = await fetch("/api/get_location_names");
        const data = await response.json();
        if (data && data.locations) {
          setLocations(data.locations);
        }
      } catch (error) {
        console.log("Using demo locations");
        // Demo locations for showcase
        setLocations([
          "Electronic City",
          "Rajaji Nagar",
          "Whitefield",
          "Koramangala",
          "Indiranagar",
          "Marathahalli",
          "HSR Layout",
          "BTM Layout",
          "Jayanagar",
          "JP Nagar"
        ]);
      }
    };
    fetchLocations();
  }, []);

  const handleEstimatePrice = async () => {
    if (!location) {
      toast({
        title: "Please select a location",
        description: "Location is required for price estimation",
        variant: "destructive",
      });
      return;
    }

    if (!sqft || parseFloat(sqft) <= 0) {
      toast({
        title: "Please enter valid area",
        description: "Square feet must be greater than 0",
        variant: "destructive",
      });
      return;
    }

    setIsLoading(true);
    
    try {
      const response = await fetch("/api/predict_home_price", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          total_sqft: sqft,
          bhk: bhk.toString(),
          bath: bathrooms.toString(),
          location: location,
        }),
      });
      
      const data = await response.json();
      setEstimatedPrice(data.estimated_price.toString());
      toast({
        title: "Price Estimated!",
        description: `Estimated price: ₹${data.estimated_price} Lakh`,
      });
    } catch (error) {
      // Demo price for showcase
      const demoPrice = (parseFloat(sqft) * 0.008 * bhk * (bathrooms * 0.5 + 1)).toFixed(2);
      setEstimatedPrice(demoPrice);
      toast({
        title: "Demo Price Calculated",
        description: "Using demo calculation (API not connected)",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="glass-card p-8 w-full max-w-md animate-slide-up" style={{ animationDelay: "0.2s" }}>
      {/* Header */}
      <div className="text-center mb-8">
        <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-primary/20 mb-4 animate-float">
          <Home className="w-8 h-8 text-primary" />
        </div>
        <h1 className="text-2xl font-bold text-foreground mb-2">
          Price Predictor
        </h1>
        <p className="text-sm text-muted-foreground">
          Bangalore Home Price Estimation
        </p>
      </div>

      {/* Form */}
      <div className="space-y-6">
        {/* Area Input */}
        <div className="space-y-2">
          <label className="flex items-center gap-2 text-sm font-medium text-foreground">
            <Calculator className="w-4 h-4 text-primary" />
            Area (Square Feet)
          </label>
          <input
            type="number"
            value={sqft}
            onChange={(e) => setSqft(e.target.value)}
            className="glass-input"
            placeholder="Enter area in sq.ft"
          />
        </div>

        {/* BHK Selection */}
        <div className="space-y-2">
          <label className="flex items-center gap-2 text-sm font-medium text-foreground">
            <Home className="w-4 h-4 text-primary" />
            BHK
          </label>
          <RadioSwitch
            name="uiBHK"
            options={[1, 2, 3, 4, 5]}
            value={bhk}
            onChange={setBhk}
          />
        </div>

        {/* Bathrooms Selection */}
        <div className="space-y-2">
          <label className="flex items-center gap-2 text-sm font-medium text-foreground">
            <Bath className="w-4 h-4 text-primary" />
            Bathrooms
          </label>
          <RadioSwitch
            name="uiBathrooms"
            options={[1, 2, 3, 4, 5]}
            value={bathrooms}
            onChange={setBathrooms}
          />
        </div>

        {/* Location Dropdown */}
        <div className="space-y-2">
          <label className="flex items-center gap-2 text-sm font-medium text-foreground">
            <MapPin className="w-4 h-4 text-primary" />
            Location
          </label>
          <div className="relative">
            <select
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              className="glass-select pr-10"
            >
              <option value="" disabled>
                Choose a Location
              </option>
              {locations.map((loc) => (
                <option key={loc} value={loc} className="bg-background text-foreground">
                  {loc}
                </option>
              ))}
            </select>
            <div className="absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none">
              <svg className="w-4 h-4 text-muted-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </div>
          </div>
        </div>

        {/* Submit Button */}
        <button
          onClick={handleEstimatePrice}
          disabled={isLoading}
          className="glass-button w-full flex items-center justify-center gap-2"
        >
          {isLoading ? (
            <div className="w-5 h-5 border-2 border-primary-foreground/30 border-t-primary-foreground rounded-full animate-spin" />
          ) : (
            <>
              <IndianRupee className="w-4 h-4" />
              Estimate Price
            </>
          )}
        </button>

        {/* Result */}
        {estimatedPrice && (
          <div className="result-card animate-fade-in">
            <p className="text-xs text-accent/80 uppercase tracking-wider mb-1">
              Estimated Price
            </p>
            <p className="text-2xl font-bold text-accent flex items-center justify-center gap-1">
              <IndianRupee className="w-5 h-5" />
              {estimatedPrice} Lakh
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default PricePredictor;
